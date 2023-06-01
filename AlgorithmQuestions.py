# // Adding this comment to enable pull request feature

# Task 1:

def isPalindrome(s):
    start = 0
    end = len(s) - 1
    s = s.lower()  # Convert string to lowercase (optional)

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


print(isPalindrome("abcdcba"))  # TRUE
print(isPalindrome("aba")) # TRUE
print(isPalindrome("c"))  # TRUE
print(isPalindrome("radar"))  # TRUE
print(isPalindrome("level"))  # TRUE
print(isPalindrome("pencil"))  # # TRUE
print(isPalindrome("ark"))  # TRUE
print(isPalindrome("aa"))  # TRUE

# The given code has a time complexity of O(n) and a space complexity of O(1), where n is the length of the input 
# string.
# The chosen approach is simple and efficient. It iterates through the string from both ends, comparing characters
#  until it reaches the middle. By doing so, it can quickly determine if the string is a palindrome or not. The 
# algorithm has a linear time complexity, which is optimal for this problem.
# The given code is already quite high efficiency, as it has a linear time complexity. It only makes n/2 
# comparisons in the worst case, which is the best we can achieve for determining if a string is a palindrome.
# However, we could have used string reversal that could be considered more efficient in terms of time complexity. 
# We could have reversed the input string and then compared it with the original string. If they were the same, the original string would be a palindrome.
# Example of approach using string reversal:

# # def is_palindrome(s):
#     reversed_s = s[::-1]
#     return s == reversed_s



