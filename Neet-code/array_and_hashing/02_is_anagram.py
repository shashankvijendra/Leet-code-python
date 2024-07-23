class Solution:
    """
    Checks if two strings are anagrams of each other.

    Two strings are considered anagrams if they contain the same characters in the same quantities,
    regardless of their order. This method compares two input strings and determines if they are anagrams.

    Parameters:
    - s (str): The first string to compare.
    - t (str): The second string to compare.

    Returns:
    - bool: True if the two strings are anagrams of each other, otherwise False.
    """    
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = 1+s_count.get(s[i],0)
            t_count[t[i]] = 1+t_count.get(t[i],0)
        
        return s_count == t_count
    
    
# Input: s = "racecar", t = "carrace"
# Output: true

# Input: s = "jar", t = "jam"
# Output: false

