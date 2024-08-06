"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height)-1
        while l<r:
            min_val = min(height[l], height[r])
            max_area = max(max_area, min_val*(r-l))
            if height[l]>=height[r]:
                r -= 1
            else:
                l += 1

        return max_area