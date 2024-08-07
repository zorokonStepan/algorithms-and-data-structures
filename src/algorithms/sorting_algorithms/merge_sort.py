"""
    Сортировка слиянием

    На входе 2 отсортированных массива.

    На каждом шаге сравниваются первые элементы массивов. Тот что меньше добавляется в итоговый
    массив. Если в одном из массивов кончились элементы, то оставшиеся элементы из другого массива
    добавляются в итоговый массив.

    Временная сложность алгоритма: O(n logn)

    Сортировка слиянием относится к категории алгоритмов «разделяй и властвуй»
"""

import math


def merging(left_array, right_array):
    new_array = []

    while min(len(left_array), len(right_array)) > 0:
        if left_array[0] > right_array[0]:
            new_array.append(right_array.pop(0))
        elif left_array[0] <= right_array[0]:
            new_array.append(left_array.pop(0))

    if len(left_array) > 0:
        new_array.extend(left_array)

    if len(right_array) > 0:
        new_array.extend(right_array)

    return new_array


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        left = merge_sort(array[: math.floor(len(array) / 2)])
        right = merge_sort(array[math.floor(len(array) / 2):])
        return merging(left, right)
