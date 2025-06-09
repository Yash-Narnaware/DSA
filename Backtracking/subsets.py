# A recursive function to print all the subsets of a given string
def subsets(str1, tmp, i, n):
    if i == n:
        print(tmp)
        return

    subsets(str1, tmp + str1[i], i + 1, n)
    subsets(str1, tmp, i + 1, n)


subsets("yash", "", 0, 4)
