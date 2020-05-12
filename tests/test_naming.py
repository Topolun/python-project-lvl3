from page_loader import modifiers


def test_name_creation():
    assert modifiers.get_name(
        'https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'
    assert modifiers.get_name(
        'https://ru.hexlet.io/courses', 'dir') == 'ru-hexlet-io-courses_files'
    assert modifiers.get_name(
        'https://ru.hexlet.io/style.css') == 'ru-hexlet-io-style.css'


def test_path_to_local():
    assert modifiers.change_path_to_local(
        'testes.txt',
        './project/tests') == './project/tests/testes.txt'


def test_path_normalize():
    assert modifiers.path_normalize_for_download(
        '/tests',
        'https://ru.hexlet.io/') == 'https://ru.hexlet.io/tests'
