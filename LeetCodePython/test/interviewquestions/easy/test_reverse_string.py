from interviewquestions.easy.reverse_integer import reverse


def test_reverse_integer_positive_input():
    num = 123
    expected_result = 321
    assert reverse(num) == expected_result


def test_reverse_integer_negative_input():
    num = -123
    expected_result = -321
    assert reverse(num) == expected_result


def test_reverse_integer_reversed_input_causes_overflow_returns_0():
    num = 2147483647
    expected_result = 0
    assert reverse(num) == expected_result
