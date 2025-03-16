from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        """Searches for `target` in sorted array `nums` using binary search.

        Args:
            nums: A sorted list of integers.
            target: The integer to search for.

        Returns:
            The index of `target` in `nums` if it exists, -1 otherwise.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            