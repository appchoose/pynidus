import pytest
from pynidus import clients

@pytest.fixture
def es_config():
    return {
        "host": "es_host",
        "user": "user",
        "password": "password"
    }

@pytest.fixture
def pg_config():
    return {
        "host": "localhost",
        "user": "user",
        "password": "password",
        "database": "database"
    }

@pytest.fixture
def gcs_config():
    return {
        "bucket": "gcs_bucket"
    }

def test_es_client(es_config):
    pass

def test_pg_client(pg_config):
    pass

def test_gcs_client():
    pass