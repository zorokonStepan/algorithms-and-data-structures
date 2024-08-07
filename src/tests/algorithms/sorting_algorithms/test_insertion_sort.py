from algorithms.sorting_algorithms.insertion_sort import insert_element_to_array, insertion_sort


def test_insert_element_to_array():
    assert insert_element_to_array([1, 2, 3, 3, 4, 6, 8, 12], 5) == [1, 2, 3, 3, 4, 5, 6, 8, 12]
    assert insert_element_to_array([5, 9, 12, 54, 555], 39) == [5, 9, 12, 39, 54, 555]


def test_insertion_sort():
    assert insertion_sort([5, 4, 15, 144, 121, 2, 3]) == [2, 3, 4, 5, 15, 121, 144]
    assert insertion_sort([1, 3, 4, 4, 5, 7, 8, 9, 2, 4, 6, 7, 8, 8, 10, 12, 13, 14]) == [
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
