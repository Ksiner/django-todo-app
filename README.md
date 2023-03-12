# Django Todo API
Test todo app on Django

### Project context

#####Tech:
- python 3.11.2
- django 4.1.7
- postgresql 13 (alpine)

#####API functionality:
- registration & authentication by email with confirmation
- user profile update
- projects:
    - projects management (CRUD depending on role on the projects)
    - projects members management (invitation, removal, role change)
    - multiple roles for project members (restrictions depending on the role of the user on a specific project)
- task management
    - tasks backlog (CRUD)
    - columns management (CRUD)
    - tasks management (CRUD)
- websockets
    - project members list
    - tasks dashboards
        - backlog
        - columns & tasks

### Contribute
In order to contribute follow these steps:

1. Clone the project
```
# https
https://github.com/Ksiner/django-todo-app.git

# ssh
git@github.com:Ksiner/django-todo-app.git
```

2. Init python venv
```
virtualenv --python="/usr/local/bin/python3" .venv

# or

python3 -m venv .venv
```

3. Install python packages
```
pip install -r requirements.txt
```

4. Before starting api server we need to run migrations firstly.
in order to run migrations we need to set database connection configs via .env file at root folder of the project.
Use `.env.example` for environment variables names list and fill them according to you localhost context
<b>Hint: You can use docker-compose to bootstrap postgresql database service:</b>
```
docker-compose -p django-todo up -d
```

5. Now we can run the migrations themselves:
```
python manage.py migrate
```

6. Finally we're can start the api server
```
python manage.py
```

7. Congratz, you're ready to go! Have a nice coding experience :)