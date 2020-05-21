# havi_task
Havi task

# Requirements
1. This project uses postgres database so it is required to have a postgres db with db name havi_task.
2. Make a python 3.7 virtualenv and install requirements from requirements.txt.
3. Run command "python manage.py migrate" to create all required tables in database.
4. To start application run command "python manage.py runserver" from base directory. Application will start on port 8000.

# Urls
1. "/": Home url containing application form.
2. "/applications/list/" : List of applicants also containing search bar to search according to fields and option to add notes. Only admin can view list and add notes.
3. "/login/" : To login into the application.
4. "/signup/" : To signup into the application.
5. "/logout/" : To logout from application.

# To create admin user.
1. run command "python manage.py createsuperuser" from base directory.
2. Enter username and password, rest of the fields can be skipped.
