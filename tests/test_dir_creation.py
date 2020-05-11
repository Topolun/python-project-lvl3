from page_loader import engine
import tempfile
import os


def test_file_creation():
    with tempfile.TemporaryDirectory() as tmp_dir:
        correct_path = os.path.join(os.path.dirname(tmp_dir), 'correct_path')
        wrong_path = os.path.join(os.path.dirname(tmp_dir), 'wrong_path')
        engine.create_dir(correct_path)
        assert os.path.exists(correct_path) == True
        assert os.path.exists(wrong_path) == False
