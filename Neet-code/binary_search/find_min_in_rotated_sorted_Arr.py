"""Find Minimum in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?"""

from typing import List

###My code ###
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0, len(nums) - 1
        mid = 0
        cur = nums[end]
        while start<=end:
            mid = start + (end-start) //2
            print(mid, end, start)
            cur = min(cur, nums[mid])
            if nums[mid]<nums[end]:
                end = mid - 1
            else:
                start = mid + 1
        return min(cur, nums[0])
  
### suggested code #####  
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0, len(nums) - 1
        mid = 0
        cur = float("inf")
        while start<=end:
            mid = start + (end-start) //2
            cur = min(cur, nums[mid])
            if nums[mid]>nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return min(cur, nums[start])

nums = [4,5,6,7]   
print(Solution().findMin(nums))


# Input: nums = [3,4,5,6,1,2]
# Output: 1

# Input: nums = [4,5,0,1,2,3]
# Output: 0

# Input: nums = [4,5,6,7]
# Output: 4

