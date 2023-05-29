'''
Question 2: -
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

'''


def isValid(s):
    # Create an array to store the frequency of each character
    arr = [0] * 26
    for char in s:
        arr[ord(char) - 97] += 1

    # Get a set of all unique non-zero frequencies
    frequencies = set(arr)
    frequencies.discard(0)

    if len(frequencies) == 1:  # If length == 1, the string is already valid
        return "YES"
    elif len(frequencies) == 2:
        a, b = frequencies
        if (abs(b - a) == 1) and (arr.count(a) == 1 or arr.count(b) == 1):
            return "YES"
        else:
            return "NO"
    else:  # If length > 2, we cannot convert the string to a valid string
        return "NO"

input_string = input("Enter a string: ")
result = isValid(input_string)
print(result)


'''
Test case
Input : str = "abbca"
Output: Yes
We can make it valid by removing the "c"

Input : str = "aabbcd"
Output: No
We need to remove at least two characters
to make it valid.

Input : str = "abc"
Output: Yes

Input : str = "abbccd"
Output: No
We are allowed to traverse the string only once.

Input : str = "abcdeedcbae"
Output: Yes
code will remove the last extra e and make it valid

Input : str = "bcdeedcbae"
Output: No
We are allowed to traverse the string only once.

Input : str = "acdeedcbae"
Output: No
We are allowed to traverse the string only once.

Input : str = "abcdedcbae"
Output: Yes
'''