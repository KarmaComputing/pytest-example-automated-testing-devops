import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

API_KEY = os.getenv("API_KEY")


def add(a, b):
    return a + b


def get_api_key():
    assert API_KEY is not None, "An empty API_KEY should never be allowed, did you forget to either add it to your .env file or, set the environment variable?"  # noqa: E501
    return API_KEY
