from page_loader import engine


def test_name_creation():
    assert engine.get_name(
        'https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'
    assert engine.get_name(
        'https://ru.hexlet.io/courses', 'dir') == 'ru-hexlet-io-courses_files'
    assert engine.get_name(
        'https://ru.hexlet.io/style.css') == 'ru-hexlet-io-style.css'
