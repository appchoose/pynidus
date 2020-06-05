import pytest
from pynidus import errors

@pytest.fixture
def bugsnag_config():
    return {
        "api_key": "bugsnag_api_key",
        "release_stage": "dev"
    }

def test_error_logger(bugsnag_config):
    
    error_logger = errors.ErrorLogger(**bugsnag_config)

    assert error_logger.api_key == "bugsnag_api_key"
    assert error_logger.release_stage == "dev"