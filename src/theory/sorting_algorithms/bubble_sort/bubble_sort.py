from typing import Sequence

from theory.sorting_algorithms.data import after_sorting_numbers, before_sorting_numbers


def bubble_sort_in_place(seq: Sequence):
    has_shifts = True

    for _ in range(len(seq)):
        if not has_shifts:
            break

        has_shifts = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                has_shifts = True


if __name__ == "__main__":
    bubble_sort_in_place(before_sorting_numbers)
    assert before_sorting_numbers == after_sorting_numbers
