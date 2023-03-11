# django-todo-app
Test todo-app on Django

Tech:
- django 4.1.7
- postgresql 13 (alpine)

API functionality:
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

