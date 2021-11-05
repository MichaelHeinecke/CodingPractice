from src.interviewquestions.easy.remove_duplicates_from_sorted_array import remove_duplicates


def test_removes_duplicates_input_empty_list():
    numbers = []

    number_of_unique_elements = remove_duplicates(numbers)

    assert number_of_unique_elements == 0


def test_removes_duplicates_input_list_with_one_element():
    numbers = [1]
    expected_numbers = [1]

    number_of_unique_elements = remove_duplicates(numbers)

    assert number_of_unique_elements == 1
    for i in range(number_of_unique_elements):
        assert numbers[i] == expected_numbers[i]


def test_removes_duplicates_input_duplicate():
    numbers = [1, 1, 2]
    expected_numbers = [1, 2, 2]

    number_of_unique_elements = remove_duplicates(numbers)

    assert number_of_unique_elements == 2
    for i in range(number_of_unique_elements):
        assert numbers[i] == expected_numbers[i]


def test_removes_duplicates_input_multiple_duplicates():
    numbers = [1, 2, 3, 4, 5, 5, 6, 6]
    expected_numbers = [1, 2, 3, 4, 5, 6, 6, 6]

    number_of_unique_elements = remove_duplicates(numbers)

    assert number_of_unique_elements == 6
    for i in range(number_of_unique_elements):
        assert numbers[i] == expected_numbers[i]
