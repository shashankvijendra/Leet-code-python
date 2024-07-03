class Solution:
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

