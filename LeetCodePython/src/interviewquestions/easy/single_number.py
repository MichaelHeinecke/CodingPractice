from typing import List


def singleNumber(nums: List[int]) -> int:
    counter = {}
    for num in nums:
        if num in counter.keys():
            value = counter.get(num) + 1
            counter[num] = value
        else:
            counter[num] = 1

    result = {k: v for k, v in counter.items() if v == 1}
    return list(result.keys())[0]
