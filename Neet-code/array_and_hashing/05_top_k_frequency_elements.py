from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            d[j] = d.get(j,0)+1
        sort_data = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [w for w,o in sort_data[:k]]

# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
