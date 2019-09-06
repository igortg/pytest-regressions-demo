import pytest

from flask_hello.app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client
