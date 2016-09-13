test:
	coverage run --source='./my_community' ./my_community/manage.py test -n $(filter-out $@, $(MAKECMDGOALS))
	coverage report

makemigrations:
	./my_community/manage.py makemigrations

migrate:
	./my_community/manage.py migrate

run: makemigrations migrate
	./my_community/manage.py runserver
