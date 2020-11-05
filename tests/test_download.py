from page_loader import engine
import tempfile
import os


FIXTURES = {
    'css': './tests/fixtures/test_site/topolun-github-io-test_download-_files/topolun-github-io-test_download-style.css',
    'jpg': './tests/fixtures/test_site/topolun-github-io-test_download-_files/topolun-github-io-test_download-test_files-jpg_test.jpg',
    'png': './tests/fixtures/test_site/topolun-github-io-test_download-_files/topolun-github-io-test_download-test_files-png_test.png',
}

TEST_DATA = {
    'css':'topolun-github-io-test_download-_files/topolun-github-io-test_download-style.css',
    'jpg': 'topolun-github-io-test_download-_files/topolun-github-io-test_download-test_files-jpg_test.jpg',
    'png': 'topolun-github-io-test_download-_files/topolun-github-io-test_download-test_files-png_test.png',
}

def test_download_page():
    with tempfile.TemporaryDirectory() as tmp_dir:
        print('PATH IS -----   ', tmp_dir)
        page = 'https://topolun.github.io/test_download/'
        engine.run(page, tmp_dir)
        with open(FIXTURES.get('css')) as correct_answer:
            with open(os.path.join(tmp_dir, TEST_DATA.get('css'))) as test_answer:
                assert test_answer.read() == correct_answer.read()
        with open(FIXTURES.get('jpg'), 'rb') as correct_answer:
            with open(os.path.join(tmp_dir, TEST_DATA.get('jpg')), 'rb') as test_answer:
                assert test_answer.read() == correct_answer.read()
        with open(FIXTURES.get('png'), 'rb') as correct_answer:
            with open(os.path.join(tmp_dir, TEST_DATA.get('png')), 'rb') as test_answer:
                assert test_answer.read() == correct_answer.read()