"""Top K Elements in List
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order."""


from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            d[j] = d.get(j,0)+1
        sort_data = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [w for w,o in sort_data[:k]]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
