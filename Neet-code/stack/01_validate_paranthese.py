"""You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }
        stack_data = []
        for c in s:
            if c not in stack:
                stack_data.append(c)
            else:
                if not stack_data:
                    return False
                if stack_data.pop() != stack.get(c):
                    return False
        return not stack_data
    

# Input: s = "[]"
# Output: true

# Input: s = "([{}])"
# Output: true
