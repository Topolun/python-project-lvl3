import logging


LOG_LEVELS = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
    }


def set_log(log_level):
    if log_level in LOG_LEVELS:
        value = LOG_LEVELS[log_level]
        logging.basicConfig(level=value)
        logging.info('Page loader is started')
    else:
        message = '''
        \rLog level '{}' is not exist. Please choose correct one
        '''.format(log_level)
        raise AttributeError(message)
