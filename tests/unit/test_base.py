import pytest
from pynidus import base

@pytest.fixture
def config():
    return {
        "postgresql": {
            "host": "localhost",
            "user": "user",
            "password": "password",
            "database": "database"
        },
        "elasticsearch": {
            "host": "es_host",
            "user": "user",
            "password": "password"
        }
    }

def test_mlt_base(config):
    pass