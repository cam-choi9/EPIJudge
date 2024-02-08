from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    res = 0
    x_abs = abs(x)

    while x_abs:
        res = res * 10 + x_abs % 10
        x_abs //= 10

    if x < 0:
        return -res

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
