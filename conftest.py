from unittest.mock import Mock
import pytest
from data import BUN_NAME, SOUSE_NAME, SOUSE_COST, BUN_COST, SOUSE_TYPE


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = BUN_NAME
    mock.get_price.return_value = BUN_COST
    return mock


@pytest.fixture()
def mock_ingredient():
    mock = Mock()
    mock.get_name.return_value = SOUSE_NAME
    mock.get_type.return_value = SOUSE_TYPE
    mock.get_price.return_value = SOUSE_COST
    return mock
