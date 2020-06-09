import pytest
import argparse
import sys
import requests
import os
import tempfile
from page_loader import modifiers
from page_loader import cli
import stat


def test_page_availability():
    with pytest.raises(SystemExit):
        cli.check_page_availability('https://hex', option='start')


def test_directory_availability():
    with pytest.raises(argparse.ArgumentTypeError):
        cli.check_path('u://asdasdsa/dasasdqw/324')


def test_write_access_dir():
    with pytest.raises(SystemExit):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.chmod(tmp_dir, stat.S_IRUSR)
            new_path = '{}/test_dir'.format(tmp_dir)
            modifiers.create_dir(new_path)


def test_write_access_file():
    with pytest.raises(SystemExit):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.chmod(tmp_dir, stat.S_IRUSR)
            new_path = '{}/test_dir'.format(tmp_dir)
            modifiers.create_file('test_file_rec', '22', new_path)
