import logging
import os
from page_loader import modifiers
from bs4 import BeautifulSoup
from progress.bar import Bar
import requests
from page_loader.errors import KnownError


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
        modifiers.write_file(
            os.path.join(dir_path, file_name),
            file_data.content,
            )
        tag[attr] = os.path.join(dir_path, file_name)
        bar.next()
    bar.finish()
    file_name = modifiers.get_name(page_adress)
    modifiers.write_file(
        os.path.join(output, file_name),
        str(page_soup),
        )
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
        raise KnownError(
            "Path '{}' does not exist. Please choose correct one"
            .format(path)
            )


def page_availability(page_adress):
    try:
        page_data = requests.get(page_adress)
        status = page_data.status_code
        if status == 200:
            return page_data
        else:
            raise KnownError(
                "can't get access to the page {}. code is {}"
                .format(
                    page_adress,
                    status,
                    )
            )
    except IOError as err:
        raise KnownError(
            "can't get access to the page {}".format(
                page_adress,
                )
            ) from err
