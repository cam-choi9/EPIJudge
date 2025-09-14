from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    count = 0

    while x:
        count ^= x & 1
        x >>= 1
    
    return count


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
