def bubble_sort(lst):
    unsorted_until_index = len(lst) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(unsorted_until_index):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = False

        unsorted_until_index -= 1
    return lst
