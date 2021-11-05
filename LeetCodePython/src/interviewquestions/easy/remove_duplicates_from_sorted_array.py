from typing import List


def remove_duplicates(nums: List[int]) -> int:
    number_of_unique_elements = 0
    last_unique_element_index = 0
    i = 0

    while i < len(nums):
        while i < len(nums) - 1:
            # advance index if following number is duplicate
            if nums[i] == nums[i + 1]:
                i += 1
            else:
                break

        nums[last_unique_element_index] = nums[i]
        i += 1
        last_unique_element_index += 1
        number_of_unique_elements += 1

    return number_of_unique_elements
