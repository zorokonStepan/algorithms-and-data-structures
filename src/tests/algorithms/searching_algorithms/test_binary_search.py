from algorithms.searching_algorithms.binary_search import binary_search


def test_binary_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 8) == 7
