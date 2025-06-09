# A recursive function to calculate the factorial
def factorial(n):
    # base case
    if n == 0:
        return 1

    # recursive step
    return n * factorial(n - 1)


print(factorial(5))
