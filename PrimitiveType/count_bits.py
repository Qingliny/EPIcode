from test_framework import generic_test


def count_bits(x):
    # TODO - you fill in here.
    num = 0
    while x:
        if x & 1:
            num += 1
        x = x >> 1
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
