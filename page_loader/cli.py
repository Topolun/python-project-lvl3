import argparse
import requests
import os
import logging
import sys


LOG_LEVELS = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
    }


def get_args():
    parser = argparse.ArgumentParser(description='Page load')
    parser.add_argument(
        '-L', '--log',
        default='ERROR', help="Set level of the log's messages"
        )
    parser.add_argument(
        '-o', '--output', type=path,
        default='.', help='path to save a file'
        )
    parser.add_argument(
        'page_adress',
        type=page_availability,
        help='adress of page for download'
        )
    return parser


def set_log(log_level):
    if log_level in LOG_LEVELS:
        value = LOG_LEVELS[log_level]
        logging.basicConfig(level=value)
        logging.info('Page loader is started')
    else:
        message = '''
        \rLog level '{}' is not exist. Please choose correct one
        '''.format(log_level)
        raise argparse.ArgumentTypeError(message)


def path(path):
    if os.path.isdir(path):
        return path
    else:
        logging.critical("Path '%s' does not exist" % path)
        logging.error("Path '%s' does not exist" % path)
        message = "Path '{}' does not exist. Please choose correct one".format(
            path)
        raise argparse.ArgumentTypeError(message)


def page_availability(page_adress, option='start'):
    try:
        page_data = requests.get(page_adress)
        status = page_data.status_code
        if status == 200:
            return page_adress, page_data
        else:
            message = "Connection error, code is {}".format(status)
            raise argparse.ArgumentTypeError(message)
    except requests.RequestException as err:
        logging.debug("Connection to  '%s' failed.\n%s", page_adress, err)
        logging.error("Connection to  '%s' failed.", page_adress)
        if option == 'start':
            sys.exit(1)
