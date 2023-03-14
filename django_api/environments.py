from enum import Enum


class EnvVars(Enum):
    """Environment Variables Enumerator"""

    # DB config env vars
    DB_HOST = "DB_HOST"
    DB_PORT = "DB_PORT"
    DB_USERNAME = "DB_USERNAME"
    DB_PASSWORD = "DB_PASSWORD"
    DB_NAME = "DB_NAME"
