"""Anagram Groups
Solved 
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different."""

from typing import List

class Solution:
    """
    Groups anagrams together from a list of strings.

    Given an array of strings, this method groups all anagrams together into sublists. An anagram is
    defined as a string that contains the exact same characters as another string, but the order of
    characters can be different. The method returns the output in any order.

    Parameters:
    - strs (List[str]): A list of strings to group by anagrams.

    Returns:
    - List[List[str]]: A list of lists containing grouped anagrams.

    Time Complexity:
    - O(NK): N is the number of strings in the input list, and K is the maximum length of a string.
      This accounts for iterating over each character in each string during the sorting and comparison steps.

    Space Complexity:
    - O(NK): Similar to the time complexity, this accounts for storing the sorted versions of strings
      and grouping them together. In the worst case, every string could be unique, requiring storage
      proportional to the total number of characters across all strings.
    """    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagrams(s, t):
            if len(s)!=len(t):
                return False
            s_count = {}
            t_count = {}
            for i in range(len(s)):
                s_count[s[i]] = 1+s_count.get(s[i],0)
                t_count[t[i]] = 1+t_count.get(t[i],0)            
            return s_count == t_count
        n = len(strs)
        data = {}
        store_dist = set()
        for i, var in enumerate(strs):
            if var in store_dist:
                continue
            store_dist.add(var)
            data[var] = [var]
            for var2 in strs[i+1:]:
                if is_anagrams(var, var2):
                    data.setdefault(var,[]).append(var2)
                    store_dist.add(var2)
        return sorted(list(data.values()), key=lambda x: len(x))
    

# Input: strs = ["x"]
# Output: [["x"]]

# Input: strs = [""]
# Output: [[""]]
