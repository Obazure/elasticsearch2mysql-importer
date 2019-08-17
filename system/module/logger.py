"""Setup logging tool."""
import logging
import os
import time
from logging.handlers import RotatingFileHandler
from system.config import logger as logger_c

loggers = {}


def setup_custom_logger(name, type):
    """Initialize the custom logger for debugging and error logging.

    Parameters
    ----------
    name : str
        Name of the logger.

    Returns
    -------
    logging.logger
        The custom logger.

    """
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        # set up logging to file - see previous section for more details
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=logger_c.config[type] + '.log',
                            filemode='w')
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

        # define a Handler which writes INFO messages or higher to the sys.stderr
        stream_handler = logging.StreamHandler()
        file_handler = logging.handlers.RotatingFileHandler(
            filename=logger_c.config[type], backupCount=logger_c.config[logger_c.LOGGER_BACKUP_COUNT])
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Check if log exists and should therefore be rolled
        needRoll = os.path.isfile(logger_c.config[type])

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        # This is a stale log, so roll it
        if needRoll:
            # Add timestamp
            logger.debug('\n---------\nLog closed on %s.\n---------\n' %
                         time.asctime())
            # Roll over on application start
            logger.handlers[0].doRollover()

        # Add timestamp
        logger.debug('\n---------\nLog started on %s.\n---------\n' %
                     time.asctime())
        loggers[name] = logger
        return logger
