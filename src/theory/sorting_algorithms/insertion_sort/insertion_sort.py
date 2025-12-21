from typing import Sequence

from theory.sorting_algorithms.data import after_sorting_numbers, before_sorting_numbers


def insertion_sort_in_place(seq: Sequence) -> Sequence:
    if len(seq) < 2:
        return seq

    index = 1

    while index < len(seq):
        insert_item = seq[index]

        for ind, item in enumerate(seq[:index]):
            if insert_item < item:
                insert_ind = index
                while insert_ind != ind:
                    seq[insert_ind], seq[insert_ind - 1] = seq[insert_ind - 1], seq[insert_ind]
                    insert_ind -= 1
                break

        index += 1

    return seq


if __name__ == "__main__":
    assert insertion_sort_in_place(before_sorting_numbers) == after_sorting_numbers
