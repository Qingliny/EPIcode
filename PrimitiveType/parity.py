from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    res = 0
    while x:
    # -----------basic------------
        res = res ^ (x&1)
        x >>= 1
    #     if x & 1:
    #         num += 1
    #     x = x >> 1
    # if num % 2 == 1:
    #     return 1
    # -----------erasing the lowest bit ------------
        res ^= 1
        x &= (x-1)   # drop the lowest set bit of x
    # -----------use mask, divide and conquer
    
    return res


if __name__ == '__main__':
    print(8&~7)
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
