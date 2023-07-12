import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


class Config:
    """Set Flask configuration vars from .env file."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
