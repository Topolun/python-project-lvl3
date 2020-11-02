import os
from bs4 import BeautifulSoup
from progress.bar import Bar
import requests
from page_loader.errors import KnownError
import urllib


SELECTORS = {
    'link': 'href',
    'script': 'src',
    'img': 'src'
}

BINARY_FILES = (
    '.png', '.gif', '.jpg', '.tiff',
    '.bmp', '.DS_Store', '.eot', '.otf',
    '.ttf', '.woff', '.rgb', '.ico',
    )


def run(page_adress, output):
    page_data, binary = page_load(page_adress)
    dir_name = get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    create_dir(dir_path)
    page_soup, links_for_download = change_HTML(
        page_data,
        page_adress,
        dir_path,
        )
    file_name = get_name(page_adress)
    message = "Page saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    bar = Bar('Processing', max=len(links_for_download) + 1)
    write_file(
        os.path.join(output, file_name),
        binary,
        str(page_soup),
        )
    bar.next()
    for link in links_for_download:
        file_data, binary = page_load(link)
        file_name = get_name(link)
        write_file(
            os.path.join(dir_path, file_name),
            binary,
            file_data,
            )
        bar.next()
    bar.finish()
    print(message)
    return None


def content_filter(tag):
    name = tag.name
    attr = SELECTORS.get(name)
    return name in SELECTORS and tag.has_attr(attr)


def page_load(page_adress):
    try:
        _, ext = os.path.splitext(page_adress)
        binary = ext in BINARY_FILES
        page_data = requests.get(page_adress)
        status = page_data.status_code
        if status == 200:
            return page_data.content, binary
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


def write_file(path, binary, data=''):
    open_method = 'wb'
    if not binary:
        open_method = 'w'
        data = str(data)
    try:
        with open(path, open_method) as new_file:
            new_file.write(data)
    except IOError as err:
        raise KnownError(
            "can't write file {}".format(path)
        ) from err


def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        try:
            os.mkdir(dir_path)
        except IOError as err:
            raise KnownError(
                "can't write file {}".format(dir_path)
            ) from err


def change_HTML(page_data, page_adress, dir_path):
    page_soup = BeautifulSoup(page_data, features="html.parser")
    tags = page_soup.find_all(content_filter)
    links_for_download = []
    for tag in tags:
        attr = SELECTORS.get(tag.name)
        normalized_path = urllib.parse.urljoin(
            page_adress,
            tag[attr],
            )
        links_for_download.append(normalized_path)
        file_name = get_name(normalized_path)
        tag[attr] = os.path.join(dir_path, file_name)
    return page_soup, links_for_download
