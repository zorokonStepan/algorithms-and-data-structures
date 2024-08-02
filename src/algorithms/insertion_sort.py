"""
    Сортировка списка методом вставки

    Элементы из списка, который нужно отсортировать, поочередно удаляются и вставляются в новый,
    изначально пустой список в отсортированном порядке.

    Временная сложность алгоритма: O(n^2)
"""

from typing import Any


def insert_element_to_array(array: list, to_insert_element: Any):
    check_location = len(array) - 1
    insert_location = 0

    while check_location >= 0:
        if to_insert_element > array[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1

    array.insert(insert_location, to_insert_element)
    return array


def insertion_sort(arr: list):
    new_arr = []

    while len(arr) > 0:
        new_arr = insert_element_to_array(new_arr, arr.pop(0))

    return new_arr
