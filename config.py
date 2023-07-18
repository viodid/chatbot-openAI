"""Flask configuration variables."""
import os


class Config:
    """Set Flask configuration vars from .env file."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    OPENAI_API_TYPE = os.environ.get('OPENAI_API_TYPE')
    OPENAI_API_VERSION = os.environ.get('OPENAI_API_VERSION')
    OPENAI_API_ENDPOINT = os.environ.get('OPENAI_API_ENDPOINT')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    OPENAI_COMPLETIONS_ENGINE = os.environ.get('OPENAI_COMPLETIONS_ENGINE')
