flake8:
	flake8 ./my_community/

test: flake8
	coverage run ./my_community/manage.py test -n $(filter-out $@, $(MAKECMDGOALS))
	coverage report

makemigrations:
	./my_community/manage.py makemigrations

migrate:
	./my_community/manage.py migrate

run:
	./my_community/manage.py runserver


${VIRTUAL_ENV}/bin/pip-sync:
	pip install pip-tools

pip-tools: ${VIRTUAL_ENV}/bin/pip-sync

pip-compile: pip-tools
	@rm -f requirements/production.txt
	pip-compile requirements/production.in

pip-install: pip-compile
	pip install --upgrade -r requirements/local.txt

pip-upgrade: pip-tools
	pip-compile --upgrade requirements/production.in
