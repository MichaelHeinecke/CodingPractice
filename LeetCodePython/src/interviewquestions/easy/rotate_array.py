from typing import List


# def rotate(array: List[int], k: int) -> None:
#     """
#     Right rotate array in-place
#     """


def rotate(array: List[int], k: int) -> None:
    rotations = k % len(array)
    temp = []

    # copy elements to move to start of array to temp list
    for i in range(len(array) - rotations, len(array)):
        temp.append(array[i])

    # move elements from left to right
    for i in range(len(array) - 1, rotations - 1, -1):
        array[i] = array[i - rotations]

    # put elements from temp to beginning of list
    for i in range(rotations):
        array[i] = temp[i]
