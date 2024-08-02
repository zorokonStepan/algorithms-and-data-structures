from algorithms.euclidean_algorithm_gcf import gcd


def test_gcd():
    assert gcd(100, 31) == 1
    assert gcd(26, 13) == 13
    assert gcd(17, 7) == 1
    assert gcd(9, 27) == 9
