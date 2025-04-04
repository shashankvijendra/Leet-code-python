# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.

 

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if ('-' in s or '+' in s) and len(s)<=1:
            return 0
        new_s = ""
        signed = ""
        for i in s:
            if i.isnumeric():
                new_s += str(i)
            elif i in ['-', '+'] and len(new_s)<1:
                if signed:
                    break
                new_s += str(i)
                signed += str(i)
            elif i in ['0',0] and len(new_s)>=1:
                new_s += str(i)
            elif i == ' ':
                break
            else:
                break
        if not new_s:
            return 0
        try:
            res = int(new_s or 0)
        except ValueError:
            return 0
        return 2**31-1 if res > 2**31-1 else max(res, -2**31)


s = Solution()
print(s.myAtoi('0-1'))


# Methode 2
def string_to_int(s: str) -> int:
    """
    Converts a string to an integer by removing non-digit characters.

    Args:
        s (str): The input string to convert.

    Returns:
        int: The converted integer, or an error message if the conversion fails.
    """
    s = ''.join(filter(str.isdigit, s))  # Remove non-digit characters
    if not s:
        return "Error: No digits found in input string"
    try:
        return int(s)
    except ValueError:
        return "Error: Invalid input string"