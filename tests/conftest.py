import pytest

@pytest.fixture(scope="module")
def custom_fixture():
    
    return [i for i in range(1, 10+1)]