from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    # Extract the i-th and j-th bits
    v1 = x >> i & 1
    v2 = x >> j & 1
    # check if they are same, not same -> swap
    # Use **BitMask** and **XOR** to flip the value.
    # x XOR 1:
    # if x == 0: x^1 = 1;
    # if x == 1: x^1 = 0;
    # to flip i-th and j-th, BitMask could use 00001000100 to flip.
    if v1 != v2:
        bitmask = (1 << i) | (1 << j)
        x ^= bitmask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
