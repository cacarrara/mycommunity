# Steps to contribute

1. Fork the project
2. Clone your fork for your machine
3. Create a local virtualenv in your machine (Python3) and install requirements `pip install -r requirements.txt`;
4. We can check our installed dependencies using `pip freeze`;
5. Make sure the project is running successfully using the command `my_community/manage.py runserver` and visiting `http://127.0.0.1:8000/`;
6. We can also use the `make` tool in conjunction with the `Makefile` at the root of our project. The above command, for example, can be launched simply as `make run`. Check out the make documentation at `https://www.gnu.org/software/make/manual/make.html`;
7. In your local repository, create a new branch to work on the issue you choose to solve. The issues can be found at `https://github.com/cacarrara/mycommunity/issues`;
8. Once the issue is solved, push the new branch with the changes to your own fork on Github;
9. Open a Pull Request from this branch to the original repository;
