from src.interviewquestions.easy.rotate_array import rotate


def test_rotate_input_two_elements_rotate_by_1():
    nums = [1, 2]
    expected_nums = [2, 1]

    rotate(nums, 1)
    assert nums == expected_nums


def test_rotate_input_four_elements_rotate_by_2():
    nums = [-1, -100, 3, 99]
    expected_nums = [3, 99, -1, -100]

    rotate(nums, 2)

    assert nums == expected_nums


def test_rotate_odd_number_of_elements_in_list_rotate_by_3():
    nums = [1, 2, 3, 4, 5, 6, 7]
    expected_nums = [5, 6, 7, 1, 2, 3, 4]

    rotate(nums, 3)

    assert nums == expected_nums


def test_rotate_odd_number_of_elements_in_list_rotate_by_4():
    nums = [1, 2, 3, 4, 5, 6, 7]
    expected_nums = [4, 5, 6, 7, 1, 2, 3]

    rotate(nums, 4)

    assert nums == expected_nums
