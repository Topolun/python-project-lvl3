install:
	poetry install

lint:
	poetry run flake8 page_loader

run:
	poetry run page_loader https://hexlet.io/courses

test:
	poetry run pytest

test_a:
	poetry run pytest -vv

publish:
	poetry publish -r test

run_err:
	poetry run page_loader https://hexl

test_site:
	poetry run page_loader https://topolun.github.io/test_download/ --output /home/topolun/python-project-lvl3/tests/fixtures/test_site
