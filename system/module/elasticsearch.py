from elasticsearch import Elasticsearch
from system.config import es
from system.config.logger import LOGGER_ES
from system.module.logger import setup_custom_logger


class ES:
    logger = None
    index = es.config[es.ES_INDEX_NAME]
    elastic = None

    scroll_id = None

    def __init__(self):
        self.logger = setup_custom_logger(LOGGER_ES, LOGGER_ES)
        self.connect_to_es()

    def connect_to_es(self):
        self.elastic = Elasticsearch([es.config])
        self.logger.debug(es.log_message[es.MSG_ES_CONNECTION_ESTABLISHED])

    def is_connection_established(self):
        if self.elastic is not None:
            self.logger.debug(es.log_message[es.MSG_ES_CONNECTION_UP])
            return True
        else:
            self.logger.debug(es.log_message[es.MSG_ES_CONNECTION_DOWN])
            return False

    def iterate_all_documents(self, pagesize=250, scroll_timeout="1m", **kwargs):
        if not self.is_connection_established():
            return None

        is_first = True
        while True:
            if is_first:
                result = self.elastic.search(index=self.index, scroll="1m", **kwargs, body={
                    "size": pagesize
                })
                is_first = False
            else:
                result = self.elastic.scroll(body={
                    "scroll_id": self.scroll_id,
                    "scroll": scroll_timeout
                })
            self.scroll_id = result["_scroll_id"]
            hits = result["hits"]["hits"]

            if not hits:
                break

            yield from (hit['_source'] for hit in hits)
