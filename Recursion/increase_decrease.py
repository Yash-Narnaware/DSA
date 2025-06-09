# A recursive functions to print number in increasing or decreasing order
def inc(n):
    if n == 0:
        return

    inc(n - 1)
    print(n)


inc(5)


def dec(n):
    if n == 0:
        return

    print(n)
    dec(n - 1)


dec(5)
