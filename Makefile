pep8:
	pep8 ./my_community/

test: pep8
	coverage run ./my_community/manage.py test -n $(filter-out $@, $(MAKECMDGOALS))
	coverage report

makemigrations:
	./my_community/manage.py makemigrations

migrate:
	./my_community/manage.py migrate

run:
	./my_community/manage.py runserver

