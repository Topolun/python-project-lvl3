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


def run(page_adress, output):
    page_data = page_load(page_adress)
    dir_name = get_name(page_adress, output='dir')
    dir_path = os.path.join(output, dir_name)
    create_dir(dir_path)
    page_soup = BeautifulSoup(page_data.content, features="html.parser")
    tags = page_soup.find_all(content_filter)
    bar = Bar('Processing', max=len(tags))
    for tag in tags:
        attr = SELECTORS.get(tag.name)
        normalized_path = path_normalize_for_download(
            tag[attr], page_adress
            )
        file_name = get_name(normalized_path)
        file_data = page_load(normalized_path)
        write_file(
            os.path.join(dir_path, file_name),
            file_data.content,
            )
        tag[attr] = os.path.join(dir_path, file_name)
        bar.next()
    bar.finish()
    file_name = get_name(page_adress)
    write_file(
        os.path.join(output, file_name),
        str(page_soup),
        )
    message = "Page saved at path: '{}'\nwith name: '{}'".format(
        os.path.abspath(output), file_name
        )
    print(message)
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


def page_load(page_adress):
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


def write_file(path, data=''):
    open_method = 'wb'
    if isinstance(data, str):
        open_method = 'w'
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
