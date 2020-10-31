import urllib
import os
import logging
import sys


def get_name(page_adress, output='file'):
    url = urllib.parse.urlparse(page_adress)
    url_host = url.hostname.replace('.', '-')
    url_path = url.path.replace('/', '-')
    _, ext = os.path.splitext(url_path)
    end = '.html'
    if output == 'dir':
        end = '_files'
    elif ext != '':
        end = ''
    name = '{}{}{}'.format(url_host, url_path, end)
    return name


def path_normalize_for_download(path, page_adress):
    return urllib.parse.urljoin(page_adress, path)


def create_file(file_name, data='', path=''):
    new_path = os.path.join(path, file_name)
    open_method = 'wb'
    if isinstance(data, str):
        open_method = 'w'
    try:
        with open(new_path, open_method) as new_file:
            new_file.write(data)
    except PermissionError as err:
        logging.debug("No write access to create '%s'\n%s", file_name, err)
        logging.error("You have no write access to create '%s'", file_name)
        sys.exit(1)


def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        try:
            os.mkdir(dir_path)
        except PermissionError as err:
            logging.debug(
                "No write access to create '%s'\n%s", dir_path, err
                )
            logging.error("You have no write access to create '%s'", dir_path)
            sys.exit(1)
