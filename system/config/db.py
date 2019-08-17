DB_HOST = 'host'
DB_DATABASE = 'database'
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_CONNECTION_TIMEOUT = 'connection_timeout'

config = {
    DB_HOST: 'localhost',
    DB_DATABASE: '<DATABASE_NAME>',
    DB_USER: 'username',
    DB_PASSWORD: 'password',
    DB_CONNECTION_TIMEOUT: 180,
}

DB_KEYWORDS_TABLE = 'keywords_table'

tables = {
    DB_KEYWORDS_TABLE: 'company_keywords',
}

DB_COMPANY_ID_COLUMN = 'company_id'
DB_KEYWORDS_COLUMN = 'keywords'

SELECT_DATABASE = 'select_db'
INSERT_QUERY = 'insertion_query'

query = {
    SELECT_DATABASE: "select database();",
    INSERT_QUERY: "INSERT INTO %s ( %s ) VALUES "
}

MSG_DB_CONNECTION_ESTABLISHED = 'connected_mysql'
MSG_DB_CONNECTED = 'connected_db'
MSG_DB_CONNECTION_UP = 'connection_up'
MSG_DB_CONNECTION_DOWN = 'connection_down'
MSG_DB_INSERTED = 'inserted'

log_message = {
    MSG_DB_CONNECTION_ESTABLISHED: "Connected to MySQL database ... MySQL Server version on %s",
    MSG_DB_CONNECTED: "You're connected to - %s",

    MSG_DB_CONNECTION_UP: "Connection to MySQL is up.",
    MSG_DB_CONNECTION_DOWN: "Connection to MySQL is down.",
    MSG_DB_INSERTED: 'Data inserted. Row id: %s.',
}
