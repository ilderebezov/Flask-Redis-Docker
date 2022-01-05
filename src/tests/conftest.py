from app import app
import pytest


@pytest.fixture
def app_init():
    return app