import argparse
import requests
import os


def get_args():
    parser = argparse.ArgumentParser(description='Page load')
    parser.add_argument(
        '-o', '--output', type=check_path,
        default='.', help='path to save a file'
        )
    parser.add_argument(
        'page_adress', type=check_page_availability, help='adress of page for download'
        )
    args = parser.parse_args()
    return args


def check_path(path):
    if os.path.isdir(path):
        return path
    else:
        message = "\nPath: '{}' is not exist. Please choose correct one".format(
            path)
        raise argparse.ArgumentTypeError(message)


def check_page_availability(page_adress):
    page_data = requests.get(page_adress)
    status = page_data.status_code
    if status == 200:
        return page_adress, page_data
    else:
        message = '''
        \rOops, something goes wrong with connection. Error code is {}\
        '''.format(status)
        raise argparse.ArgumentTypeError(message)

