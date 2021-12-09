from interviewquestions.easy.intersection_of_two_arrays import intersect


def test_intersection_of_two_arrays():
    array1 = [1, 2, 3]
    array2 = [4, 2]
    assert intersect(array1, array2) == [2]


def test_intersection_of_two_arrays_2():
    array1 = [1, 2, 2, 1]
    array2 = [2, 2]
    assert intersect(array1, array2) == [2, 2]

