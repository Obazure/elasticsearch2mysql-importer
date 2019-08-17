ES_HOST = 'host'
ES_PORT = 'port'

ES_INDEX_NAME = 'index_name'
ES_TYPE_NAME = 'type_name'

config = {
    ES_HOST: 'localhost',
    ES_PORT: 9200,
    ES_INDEX_NAME: '<INDEX_NAME>',
    ES_TYPE_NAME: '<TYPE_NAME>',
}

MSG_ES_CONNECTION_ESTABLISHED = 'connected_es'
MSG_ES_CONNECTION_UP = 'connection_up'
MSG_ES_CONNECTION_DOWN = 'connection_down'

log_message = {
    MSG_ES_CONNECTION_ESTABLISHED: "Connected to Elastic Search",
    MSG_ES_CONNECTION_UP: "Connection to Elastic Search is up.",
    MSG_ES_CONNECTION_DOWN: "Connection to Elastic Search is down.",

}
