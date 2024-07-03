# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = {}
        for i in range(numRows):
            res[i+1] = ''
        temp = []
        vs = []
        is_empty = False
        index_val = 0
        for i in s:
            if is_empty and index_val>=0:
                list_val = ['']*numRows
                list_val[index_val-2] = i
                index_val -= 1
                temp.append(list_val)
            elif len(vs)<numRows:
                vs.append(i)
                is_empty = False
            if len(vs) == numRows:
                temp.append(vs)
                vs = []
                is_empty = True
                index_val = numRows
        print(temp)
        
        return 

s = 'PAYPALISHIRING'
numRows = 3
print(Solution().convert(s, numRows))