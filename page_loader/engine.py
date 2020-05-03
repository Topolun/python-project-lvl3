import requests
import urllib
import os


def create_file(file_name, data='', path=''):
    new_path = os.path.join(path, file_name)
    with open(new_path, 'w') as new_file:
        new_file.write(data)


def run(data, output):
    page_adress, page_data = data
    url = urllib.parse.urlparse(page_adress)
    url_host = url.hostname.replace('.', '-')
    url_path = url.path.replace('/', '-')
    file_name = '{}{}.html'.format(url_host, url_path)
    create_file(file_name, page_data.text, output)
    message = "File '{}' saved at path '{}'".format(
        file_name, os.path.abspath(output)
        )
    return message
