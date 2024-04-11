import pytest
from main import app

@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    with app.test_client() as client:
        yield client

    # clean up / reset resources here