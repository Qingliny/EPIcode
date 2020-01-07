from test_framework import generic_test

def swap(x,i,j):
    bitmask = (1<<i)|(1<<j)
    x = x^bitmask
    return x
def closest_int_same_bit_count(x):
    # TODO - you fill in here.
    res = 0
    for i in range(63):
        if (x>>i)&1 != (x>>(i+1))&1:
            return swap(x,i,i+1)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
