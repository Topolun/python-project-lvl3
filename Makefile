install:
	poetry install


lint:
	poetry run flake8 brain_games


run:
	poetry run page_loader https://hexlet.io/courses

test:
	poetry run pytest

test_a:
	poetry run pytest -vv

publish:
	poetry publish -r test
