import requests
import os
from page_loader import modifiers
from bs4 import BeautifulSoup


SELECTORS = {
    'link': 'href',
    'script': 'src',
    'img': 'src'
}


def run(data, output):
    page_adress, page_data = data
    dir_name = modifiers.get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    modifiers.create_dir(dir_path)
    page_soup = BeautifulSoup(page_data.content, features="html.parser")
    tags = page_soup.find_all(content_filter)
    for tag in tags:
        attr = SELECTORS.get(tag.name)
        normalized_path = modifiers.path_normalize_for_download(
            tag[attr], page_adress
            )
        file_name = modifiers.get_name(normalized_path)
        modifiers.create_file(
            file_name,
            requests.get(normalized_path).content,
            dir_path
            )
        tag[attr] = modifiers.change_path_to_local(file_name, dir_path)
    file_name = modifiers.get_name(page_adress)
    modifiers.create_file(file_name, str(page_soup), output)
    message = "Page saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    return message


def content_filter(tag):
    name = tag.name
    attr = SELECTORS.get(name)
    return name in SELECTORS and tag.has_attr(attr)
