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
    if url_host == '':
        url_host = 'ru.hexlet.io'
    url_host = url.hostname.replace('.', '-')
    url_path = url.path.replace('/', '-')
    ext = os.path.splitext(url_path)[1]
    end = '.html'
    if output == 'dir':
        end = '_files'
    elif ext is not '':
        end = ''
    name = '{}{}{}'.format(url_host, url_path, end)
    return name


def content_download(tag, path=''):
    for key, value in SELECTORS.items():
        if tag.name == key and tag.has_attr(value):
            adress = tag[value]
            print('ADRESS', adress)
            data = requests.get(adress)
            name = get_name(adress, path)
            create_file(name, data.text, path)
            #tag[value] = '&&&'
            return True

def run(data, output):
    page_adress, page_data = data
    file_name = get_name(page_adress)
    create_file(file_name, page_data.text, output)
    dir_name = get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    create_dir(dir_path)
    print(dir_path)
    selector = lambda x: content_download(x, path=dir_path)
    soup = BeautifulSoup(page_data.content)
    soup.find_all(selector)
    message = "Data saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    return message
