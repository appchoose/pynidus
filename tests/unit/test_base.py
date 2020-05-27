import pytest
from pynidus import base

@pytest.fixture
def config():
    return {
        "POSTGRESQL": {
            "HOST": "localhost",
            "USER": "user",
            "PASSWORD": "password",
            "DATABASE": "database"
        },
        "ELASTICSEARCH": {
            "HOST": "es_host",
            "USER": "user",
            "PASSWORD": "password"
        }
    }

def test_mlt_base(config):
    
    mlt = base.MLTBase(
        es_config=config.get("ELASTICSEARCH"),
        pg_config=config.get("POSTGRESQL")
    )

    assert mlt.es_client.host == "es_host"
    assert mlt.pg_client.user == "user"