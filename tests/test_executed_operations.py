import pytest
from course_project_3 import executed_operations


@pytest.fixture
def input_list():
    return [
            {'state': 'EXECUTED', 'id': 441945886},
            {'state': 'CANCELED', 'id': 638231325},
            {'state': 'CANCELED', 'id': 153863158},
            {'state': 'EXECUTED', 'id': 231354132}
            ]


def test_get_executed_operations(input_list):
    assert executed_operations.get_executed_operations(input_list) == [
            {'state': 'EXECUTED', 'id': 441945886},
            {'state': 'EXECUTED', 'id': 231354132}
            ]
