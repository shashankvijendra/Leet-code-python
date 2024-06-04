# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        print(x, (-2**32)-1 < x)
        if (-2**32)-1 > x > (2**32):
            return 0        
        if '-' in str(x):
            return int(str(x).replace('-','').strip('0')[::-1])*-1
        return int(str(x).strip('0')[::-1])

s = Solution()
print(s.reverse(123))