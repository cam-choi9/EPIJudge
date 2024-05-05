from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    result = 0

    # while x:
    #     result = result ^ (x & 1)
    #     x = x >> 1
    #
    # return result

    count = 0

    while x:
        count += 1
        x &= x-1

    return count % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
