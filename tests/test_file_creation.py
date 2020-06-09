from page_loader import modifiers
import tempfile
import os


def test_file_creation():
    with tempfile.TemporaryDirectory() as tmp_dir:
        new_path = os.path.join(os.path.dirname(tmp_dir), 'test_file')
        modifiers.create_file('test_file', '1234', os.path.dirname(tmp_dir))
        with open(new_path, 'r') as test_file:
            assert test_file.read() == '1234'
