from page_loader import engine
import tempfile


def test_file_creation():
    with tempfile.TemporaryDirectory() as tmp_dir:
        engine.create_file('test_file', '1234', tmp_dir)
        with open('test_file', 'r') as test_file:
            assert test_file.read() == '1234'
