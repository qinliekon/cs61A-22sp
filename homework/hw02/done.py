from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: x * 3

increment = lambda x: x + 1


HW_SOURCE_FILE=__file__

def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    def repeater(x):
        k = 0
        while k < n:
            x, k = f(x), k + 1
        return x
    return repeater

print(make_repeater(square, 2)(5))