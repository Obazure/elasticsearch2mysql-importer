from mysql.connector import MySQLConnection, Error

from system.config import db
from system.config.logger import LOGGER_DB
from system.module.logger import setup_custom_logger


class DB:
    connection = None
    cursor = None
    logger = None

    def __init__(self):
        self.logger = setup_custom_logger(LOGGER_DB, LOGGER_DB)
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.connection = MySQLConnection(**db.config)

            if self.connection and self.connection.is_connected():
                db_info = self.connection.get_server_info()
                self.logger.debug(db.log_message[db.MSG_DB_CONNECTION_ESTABLISHED] % db_info)

                self.cursor = self.connection.cursor()
                self.cursor.execute(db.query[db.SELECT_DATABASE])
                table_name = self.cursor.fetchone()
                self.logger.debug(db.log_message[db.MSG_DB_CONNECTED] % str(table_name))

        except Error as e:
            self.logger.exception(e)

    def is_connection_established(self):
        if self.connection is not None:
            self.logger.debug(db.log_message[db.MSG_DB_CONNECTION_UP])
            return True
        else:
            self.logger.debug(db.log_message[db.MSG_DB_CONNECTION_DOWN])
            return False

    def put(self, table, columns, values):
        if not self.is_connection_established():
            return None

        try:
            placeholder = ','.join(['%s' for i in range(len(values))])
            query = db.query[db.INSERT_QUERY] % (table, columns) + ('(%s)' % placeholder)
            self.cursor.execute(query, values)
            self.connection.commit()
            self.logger.debug(db.log_message[db.MSG_DB_INSERTED] % self.cursor.lastrowid)
        except Error as e:
            self.logger.exception(e)
