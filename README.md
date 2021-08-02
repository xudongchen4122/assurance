How to run this project:

1) Download the project from https://github.com/xudongchen4122/assurance
2) In MacOS or Linux environment, open terminal or bash shell
3) CD to assurance folder (where the project resides)
4) "ls" to make sure env folder is there
5) run the command "source env/bin/activate"
6) run the command "python3 -m pip install -r requirements.txt"
7) run the command "python3 manage.py runserver"
8) open Chrome browser, go to http://127.0.0.1:8000/
9) Sign up as a user
10) click on one of the "Start Game" buttons
11) Open Firefox browser on the same machine, or any browser on a different machine
12) Sign up as another user and join the game the first person just started
13) Keep playing
14) It allows many people to play at the same time


How to run unit tests:
1) Make sure you are still in the virtual environment (check "how to run this project" above)
2) run the command "export DJANGO_SETTINGS_MODULE=setup.settings"
3) run the command "pytest"