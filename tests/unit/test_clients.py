import pytest
from pynidus import clients

@pytest.fixture
def es_config():
    return {
        "HOST": "es_host",
        "USER": "user",
        "PASSWORD": "password"
    }

@pytest.fixture
def pg_config():
    return {
        "HOST": "localhost",
        "USER": "user",
        "PASSWORD": "password",
        "DATABASE": "database"
    }

@pytest.fixture
def gcs_config():
    return {
        "BUCKET": "gcs_bucket"
    }

def test_es_client(es_config):
    es_client = clients.ElasticsearchClient(config=es_config)
    assert es_client.host == "es_host"
    assert es_client.user == "user"
    assert es_client.password == "password"

def test_pg_client(pg_config):
    pg_client = clients.DatabaseClient(config=pg_config)
    assert pg_client.host == "localhost"
    assert pg_client.user == "user"
    assert pg_client.password == "password"
    assert pg_client.database == "database"

def test_gcs_client():
    pass