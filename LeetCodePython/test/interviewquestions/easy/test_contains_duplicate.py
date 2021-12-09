from interviewquestions.easy.contains_duplicate import containsDuplicate


def test_contains_duplicate_duplicate_returns_true():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert containsDuplicate(nums) is True


def test_contains_duplicate_no_duplicate_returns_false():
    nums = [1, 2, 3, 4]
    assert containsDuplicate(nums) is False
