from typing import Any, Sequence

from theory.sorting_algorithms.data import after_sorting_numbers, before_sorting_numbers


def selection_sort_in_place(seq: Sequence) -> None:
    if len(seq) < 2:
        return None

    index = 0

    while index < len(seq):
        min_value, _index = _min(seq[index:], index)

        while _index > index:
            seq[_index], seq[_index - 1] = seq[_index - 1], seq[_index]

            _index -= 1

        index += 1

    return None


def _min(seq: Sequence, index: int) -> tuple[int, Any]:
    min_value, min_value_index = seq[0], 0

    cur_index = 0
    while cur_index < len(seq):
        if seq[cur_index] < min_value:
            min_value, min_value_index = seq[cur_index], cur_index

        cur_index += 1

    return min_value, min_value_index + index


if __name__ == "__main__":
    selection_sort_in_place(before_sorting_numbers)
    assert before_sorting_numbers == after_sorting_numbers
