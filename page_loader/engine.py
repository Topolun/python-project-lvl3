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
    open_method = 'wb'
    if isinstance(data, str):
        open_method = 'w'
    with open(new_path, open_method) as new_file:
        new_file.write(data)


def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)



def get_name(page_adress, output='file'):
    url = urllib.parse.urlparse(page_adress)
    url_host = url.hostname.replace('.', '-')
    url_path = url.path.replace('/', '-')
    ext = os.path.splitext(url_path)[1]
    end = '.html'
    if output == 'dir':
        end = '_files'
    elif ext is not '':
        end = ''
    name = '{}{}{}'.format(url_host, url_path, end)
    print('Name: ---- ', name)
    return name


def change_path_to_local(file_name, local_path):
    return '{}/{}'.format(local_path, file_name)


def path_normalize_for_download(path, page_adress):
    return urllib.parse.urljoin(page_adress, path)

def content_filter(tag):
    name = tag.name
    attr = SELECTORS.get(name)
    return name in SELECTORS and tag.has_attr(attr)


def run(data, output):
    page_adress, page_data = data
    dir_name = get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    create_dir(dir_path)
    soup = BeautifulSoup(page_data.content)
    tags = soup.find_all(content_filter)
    for tag in tags:
        print('NEW TAG', tag.name)
        attr = SELECTORS.get(tag.name)
        normalized_path = path_normalize_for_download(tag[attr], page_adress)
        print('NORMALIZED PATH: ---------', normalized_path)
        file_name = get_name(normalized_path)
        create_file(file_name, requests.get(normalized_path).content, dir_path)
        tag[attr] = change_path_to_local(file_name, dir_path)
        print(tag[attr])
    file_name = get_name(page_adress)
    create_file(file_name, str(soup), output)
    message = "Data saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    return message
