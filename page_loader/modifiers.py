import urllib
import os


def get_name(page_adress, output='file'):
    url = urllib.parse.urlparse(page_adress)
    url_host = url.hostname.replace('.', '-')
    url_path = url.path.replace('/', '-')
    ext = os.path.splitext(url_path)[1]
    end = '.html'
    if output == 'dir':
        end = '_files'
    elif ext != '':
        end = ''
    name = '{}{}{}'.format(url_host, url_path, end)
    print('Name: ---- ', name)
    return name


def change_path_to_local(file_name, local_path):
    return '{}/{}'.format(local_path, file_name)


def path_normalize_for_download(path, page_adress):
    return urllib.parse.urljoin(page_adress, path)


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
