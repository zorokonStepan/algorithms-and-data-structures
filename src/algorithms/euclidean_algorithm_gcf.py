"""
    Алгоритм Евклида НОД

    Делить большее число на меньшее, до тех пор пока остаток от деления не станет равным нулю.
    Когда остаток от деления равен нулю меньшее число и есть наибольший общий делитель.
"""


def gcd(x, y):
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    if remainder == 0:
        return smaller

    if remainder != 0:
        return gcd(smaller, remainder)
