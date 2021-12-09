from interviewquestions.easy.first_unique_character_in_string import firstUniqChar


def test_firstUniqChar_no_unique_character_returns_minus_one():
    string = 'aabb'
    assert firstUniqChar(string) == -1


def test_firstUniqChar_unique_character_returns_index_of_first_occurrence():
    string = 'leetcode'
    assert firstUniqChar(string) == 0


def test_firstUniqChar_unique_character_returns_index_of_first_occurrence_2():
    string = 'loveleetcode'
    assert firstUniqChar(string) == 2
