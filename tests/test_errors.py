import pytest
import argparse
import sys
import requests
import os
import tempfile
from page_loader import modifiers
from page_loader import cli
from page_loader import engine
import stat
from page_loader.errors import KnownError


def test_page_load():
    with pytest.raises(KnownError):
        engine.page_load('https://httpbin.org/status/400')


def test_directory_availability():
    with pytest.raises(KnownError):
        engine.path('u://asdasdsa/dasasdqw/324')


def test_write_access_dir():
    with pytest.raises(KnownError):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.chmod(tmp_dir, stat.S_IRUSR)
            new_path = os.path.join(tmp_dir, 'test_dir')
            modifiers.create_dir(new_path)


def test_write_access_file():
    with pytest.raises(KnownError):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.chmod(tmp_dir, stat.S_IRUSR)
            new_path = '{}/test_dir'.format(tmp_dir)
            modifiers.write_file(
                os.path.join(new_path, 'test_file_rec'),
                '22',
                )
