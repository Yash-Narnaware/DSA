# A recursive functions to calculate the nth power of x

# basic method
def pow1(x, n):
    if n == 0:
        return 1

    return x * pow1(x, n - 1)


print(pow1(2, 4))


# fast method
# basically 2^5 = 2 * 2^2 * 2^2
# and 2^4 = 2^2 * 2^2
def pow2(x, n):
    if n == 0:
        return 1

    tmp = pow2(x, n // 2)
    sqr = tmp * tmp

    if n % 2 == 0:
        return sqr
    else:
        return x * sqr


print(pow2(2, 5))
