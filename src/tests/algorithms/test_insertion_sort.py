from algorithms.sorting_algorithms.insertion_sort import insert_element_to_array, insertion_sort


def test_insert_element_to_array():
    assert insert_element_to_array([1, 2, 3, 3, 4, 6, 8, 12], 5) == [1, 2, 3, 3, 4, 5, 6, 8, 12]
    assert insert_element_to_array([5, 9, 12, 54, 555], 39) == [5, 9, 12, 39, 54, 555]


def test_insertion_sort():
    assert insertion_sort([5, 4, 15, 144, 121, 2, 3]) == [2, 3, 4, 5, 15, 121, 144]
