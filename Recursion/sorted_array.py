# Recursive functions to check if given array is sorted or not


# Index based checking
def sorted_arr(arr, i, n):
    if i == n:
        return True

    return arr[i - 1] <= arr[i] and sorted_arr(arr, i + 1, n)


print(sorted_arr([1, 1, 2, 3, 4, 5], 1, 6))


# Passing the remaining array in each recursive call
def sorted_arr1(arr):
    if len(arr) == 1:
        return True

    return arr[0] <= arr[1] and sorted_arr1(arr[1:])


print(sorted_arr1([1, 1, 2, 3, 4, 5]))
