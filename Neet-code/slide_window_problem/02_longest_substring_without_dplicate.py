""" Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        val = 0
        n = 0
        l = 0
        set_data = set()
        while n<len(s):
            print(val)
            while s[n] in set_data:
                set_data.remove(s[l])
                l += 1
            set_data.add(s[n])
            val = max(val, len(set_data))
            n+=1
        return val
    

# Input: s = "zxyzxyz"
# Output: 3

# Input: s = "xxxx"
# Output: 1

