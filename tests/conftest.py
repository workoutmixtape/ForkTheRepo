import pytest

from src import app


@pytest.fixture
def client():
    app.app.config.from_object('src.conf.TestConf')
    with app.app.test_client() as client:
        yield client
