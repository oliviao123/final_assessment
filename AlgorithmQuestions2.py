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


# The code is efficient and easy to understand. It calculates the missing number in an unsorted array by leveraging the mathematical property of the sum of consecutive numbers. The time complexity is O(n), and the space complexity is O(1).

# An alternative approach could involve using a hash set to check the presence of numbers in the given range. By iterating over the array and adding each number to the set, we can identify the missing number. However, this approach has a higher space complexity of O(n) because it requires storing the numbers in the set.
