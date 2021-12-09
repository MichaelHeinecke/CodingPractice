import pytest

from interviewquestions.easy.single_number import singleNumber


@pytest.fixture
def input_array():
    return [1, 2, 2]


def test_single_number(input_array):
    result = singleNumber(input_array)
    assert result == 1