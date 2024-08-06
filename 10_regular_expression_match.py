"""Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""

import re
from time_calculator import timeit
class Solution:
    @timeit
    def isMatch(self, s: str, p: str) -> bool:
        if '.' not in p and '*' not in p and len(s) != len(p):
            return False
        try:
            if s in re.findall(p,s):
                return True
        except :
            if s in re.findall(p.replace("**",""),s):
                return True
        return False

obj = Solution()
s="abc"
p="a***abc"
print(obj.isMatch(s,p))
