from algorithms.sorting_algorithms.merge_sort import merge_sort, merging


def test_merging():
    left = [1, 3, 4, 4, 5, 7, 8, 9]
    right = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
    assert merging(left, right) == [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10, 12, 13, 14]


def test_insertion_sort():
    assert merge_sort([5, 4, 15, 144, 121, 2, 3]) == [2, 3, 4, 5, 15, 121, 144]
    assert merge_sort([1, 3, 4, 4, 5, 7, 8, 9, 2, 4, 6, 7, 8, 8, 10, 12, 13, 14]) == [
        1,
        2,
        3,
        4,
        4,
        4,
        5,
        6,
        7,
        7,
        8,
        8,
        8,
        9,
        10,
        12,
        13,
        14,
    ]
