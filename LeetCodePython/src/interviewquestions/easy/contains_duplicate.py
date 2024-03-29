import collections
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    counter = collections.Counter(nums)
    for k, v in counter.items():
        if v > 1:
            return True
    return False
