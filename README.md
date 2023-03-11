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

1. clone the project
```
# https
https://github.com/Ksiner/django-todo-app.git

# ssh
git@github.com:Ksiner/django-todo-app.git
```

2. init python venv
```
virtualenv --python="/usr/local/bin/python3" .venv

# or

python3 -m venv .venv
```

3. install python packages
```
pip install -r requirements.txt
```

4. Congratz, you're ready to go! Have a nice coding experience :)