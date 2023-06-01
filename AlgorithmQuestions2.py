def isMissing(arr):
    if not all(isinstance(num, int) for num in arr):
        raise ValueError("Invalid input, non-numeric value detected")

    n = len(arr) + 1  # Expected length of the array with the missing number
    expected_sum = (n * (n + 1)) // 2  # Sum of numbers from 1 to n

    arr_sum = sum(arr)  # Sum of the elements in the array
    missing_number = expected_sum - arr_sum

    return missing_number

print(isMissing([1, 2, 3, 4, 5]))  # nothing is missing
print(isMissing([4,5,1,3, 5, 6])) #  2 is missing
print(isMissing([ 1, 3, 7, 5, 6, 2 ])) #  4 is missing
print(isMissing([4,5,-1,3, 5]))  # THROW ERROR Invalid input, non-numeric value detected
print(isMissing([ 1, 3, 7, 5, 6, 2 ])) #  THROW ERROR Invalid input, non-numeric value detected


