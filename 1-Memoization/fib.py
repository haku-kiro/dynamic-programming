# Write a function `fib(n)` that takes in a number as an argument.
# The function should return the n-th number in the Fibonacci sequence
# Ex: Fibonacci: 1,1,2,3,5,8,13,21, etc
#             n: 1,2,3,4,5,6,7 ,8
def fib_without_memoization(n):
    """
    Doesn't make use of memoization to return the nth number of
    Fibonacci
    This function has a time complexity of O(2^n)
    and a space complexity of O(n)
    """
    if n <= 2:
        return 1

    return fib_without_memoization(n-1) + fib_without_memoization(n - 2)


def fib(n, memo={}):
    """
    Makes use of memoization to store previously calculated values
    and return those instead of spawning of more recursive calls
    onto the stack.

    We'll be using a dictionary to store previously computed results.
    This functions time complexity is O(n)
    and it's space complexity is O(n) as well
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


if __name__ == "__main__":
    # if we were to change testData to something like 50
    # the execution time would increase quite a lot.
    testData = 6
    expected = 8

    # Testing the logic without memoization
    got = fib_without_memoization(testData)
    print(got)

    assert got == expected, "Values did not match"

    # Testing the logic with memoization
    t = 50
    e = 12586269025

    # We now see that the value computes practically instantly
    got = fib(t)

    print(got)

    assert got == e, "Values did not match"
