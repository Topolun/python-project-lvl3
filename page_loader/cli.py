import argparse
import requests
import os
import logging

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
        '-L', '--log', type=set_log,
        default='CRITICAL', help="Set level of the log's messages"
        )
    parser.add_argument(
        '-o', '--output', type=check_path,
        default='.', help='path to save a file'
        )
    parser.add_argument(
        'page_adress',
        type=check_page_availability,
        help='adress of page for download'
        )
    args = parser.parse_args()
    return args


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


def check_path(path):
    if os.path.isdir(path):
        return path
    else:
        logging.critical('Path does not exist')
        message = "Path '{}' does not exist. Please choose correct one".format(
            path)
        raise argparse.ArgumentTypeError(message)


def check_page_availability(page_adress):
    page_data = requests.get(page_adress)
    status = page_data.status_code
    if status == 200:
        return page_adress, page_data
    else:
        logging.critical('Connection failed')
        message = '''
        \rOops, something goes wrong with connection. Error code is {}\
        '''.format(status)
        raise argparse.ArgumentTypeError(message)
