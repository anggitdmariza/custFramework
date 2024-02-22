import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

def pytest_configure(config):
    config.option.metadata = {
        'Project Name': 'nop Commerce',
        'Module Name': 'user',
        'Tester': 'anggit'
    }

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)