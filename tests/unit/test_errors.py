import pytest
from pynidus import errors

@pytest.fixture
def bugsnag_config():
    return {
        "API_KEY": "bugsnag_api_key",
        "RELEASE_STAGE": "dev"
    }

def test_error_logger(bugsnag_config):
    
    error_logger = errors.ErrorLogger(config=bugsnag_config)

    assert error_logger.api_key == "bugsnag_api_key"
    assert error_logger.release_stage == "dev"