def sorted_squared_array(arr):
    result = []

    for i in range(len(arr)):
        result.append(arr[i] * arr[i])

    result.sort()
    return result


def sorted_squared_array_2_pointers(arr):
    n = len(arr)
    i = 0
    j = n - 1
    result = [0] * n

    while n > 0:
        n -= 1
        left_square = arr[i] ** 2
        right_square = arr[j] ** 2
        if left_square <= right_square:
            result[n] = right_square
            j -= 1
        else:
            result[n] = left_square
            i += 1

    return result


def is_monotonic(array):
    # empty array or single element only will be monotonic
    if len(array) < 2:
        return True

    is_increasing = 0

    for i in range(len(array) - 1):
        # check monotonic increasing or decreasing
        if is_increasing == 0 and array[i] != array[i + 1]:
            is_increasing = 1 if array[i + 1] > array[i] else -1

        if is_increasing == 1 and array[i] > array[i + 1]:
            return False

        if is_increasing == -1 and array[i] < array[i + 1]:
            return False

    return True
