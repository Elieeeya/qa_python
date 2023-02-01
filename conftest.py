import pytest
from main import BooksCollector



@pytest.fixture(scope="function")
#collection books
def cb():
    yield BooksCollector()