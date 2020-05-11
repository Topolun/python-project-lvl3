import requests
import urllib
import os
from bs4 import BeautifulSoup


SELECTORS = {
    'link': 'href',
    'script': 'src',
    'img': 'src'
}


def create_file(file_name, data='', path=''):
    new_path = os.path.join(path, file_name)
    with open(new_path, 'w') as new_file:
        new_file.write(data)


def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)



def get_name(page_adress, output='file'):
    url = urllib.parse.urlparse(page_adress)
    url_host = url.hostname
    if url_host == None:
        url_host = 'ru.hexlet.io'
    url_host = url_host.replace('.', '-')
    url_path = url.path.replace('/', '-')
    ext = os.path.splitext(url_path)[1]
    end = '.html'
    if output == 'dir':
        end = '_files'
    elif ext is not '':
        end = ''
    name = '{}{}{}'.format(url_host, url_path, end)
    return name


def change_path_to_local(path, local_path):
    url = urllib.parse.urlparse(path)
    name = get_name(url.path)
    return '{}/{}'.format(local_path, name)


def path_normalize_for_download(path, page_adress):
    return urllib.parse.urljoin(page_adress, path)

def content_filter(tag):
    name = tag.name
    attr = SELECTORS.get(name)
    return name in SELECTORS and tag.has_attr(attr)


def run(data, output):
    page_adress, page_data = data
    file_name = get_name(page_adress)
    create_file(file_name, page_data.text, output)
    dir_name = get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    create_dir(dir_path)
    soup = BeautifulSoup(page_data.content)
    tags = soup.find_all(content_filter)
    for tag in tags:
        attr = SELECTORS.get(tag.name)
        normalized_path = path_normalize_for_download(tag[attr], page_adress)
        create_file(get_name(normalized_path), requests.get(normalized_path).text, dir_path)
        tag[attr] = change_path_to_local(normalized_path, dir_path)
        print(tag[attr])
    file_name = get_name(page_adress)
    create_file(file_name, str(soup), output)
    message = "Data saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    return message
