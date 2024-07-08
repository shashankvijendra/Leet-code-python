class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if len(strs)==1:
            return [strs]
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
