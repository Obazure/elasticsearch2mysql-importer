import json
from time import sleep
from system.config import db


def es2mysql_importer(context):
    for elastic_document in context.es.iterate_all_documents():
        fields = ' %s, %s ' % (db.DB_COMPANY_ID_COLUMN, db.DB_KEYWORDS_COLUMN)
        content = (str(elastic_document[db.DB_COMPANY_ID_COLUMN]), str(json.dumps(elastic_document)))
        context.db.put(db.tables[db.DB_KEYWORDS_TABLE], fields, content)
        sleep(0.1)
