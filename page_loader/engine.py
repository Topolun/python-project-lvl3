import logging
import os
import sys
from page_loader import modifiers
from bs4 import BeautifulSoup
from progress.bar import Bar
import requests


SELECTORS = {
    'link': 'href',
    'script': 'src',
    'img': 'src'
}


def run(data, output):
    page_adress = data
    page_data = page_availability(data)
    dir_name = modifiers.get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    modifiers.create_dir(dir_path)
    page_soup = BeautifulSoup(page_data.content, features="html.parser")
    tags = page_soup.find_all(content_filter)
    bar = Bar('Processing', max=len(tags))
    for tag in tags:
        logging.warning('download from tag %s' % tag)
        attr = SELECTORS.get(tag.name)
        normalized_path = modifiers.path_normalize_for_download(
            tag[attr], page_adress
            )
        file_name = modifiers.get_name(normalized_path)
        file_data = page_availability(normalized_path)
        modifiers.create_file(
            file_name,
            file_data.content,
            dir_path
            )
        tag[attr] = modifiers.change_path_to_local(file_name, dir_path)
        bar.next()
    bar.finish()
    file_name = modifiers.get_name(page_adress)
    modifiers.create_file(file_name, str(page_soup), output)
    message = "Page saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    logging.info('Logging:\n%s' % message)
    return message


def content_filter(tag):
    name = tag.name
    attr = SELECTORS.get(name)
    return name in SELECTORS and tag.has_attr(attr)


def path(path):
    if os.path.isdir(path):
        return path
    else:
        logging.critical("Path '%s' does not exist" % path)
        logging.error("Path '%s' does not exist" % path)
        message = "Path '{}' does not exist. Please choose correct one".format(
            path)
        raise AttributeError(message)


def page_availability(page_adress, option='start'):
    try:
        page_data = requests.get(page_adress)
        status = page_data.status_code
        if status == 200:
            return page_data
        else:
            message = "Connection error, code is {}".format(status)
            raise AttributeError(message)
    except requests.RequestException as err:
        logging.debug("Connection to  '%s' failed.\n%s", page_adress, err)
        logging.error("Connection to  '%s' failed.", page_adress)
        if option == 'start':
            sys.exit(1)
