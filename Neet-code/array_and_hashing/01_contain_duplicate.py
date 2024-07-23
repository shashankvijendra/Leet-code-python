from typing import List

class Solution:
    """
        Determines if a list contains any duplicate integers.

        This method checks if there are any duplicate values within the input list of integers.
        It uses a set data structure to efficiently check for duplicates because adding an element
        that already exists in the set will not change the size of the set. If the length of the set
        is less than the length of the original list, then there were duplicates present.

        Parameters:
        - nums: List[int] -- A list of integers to search for duplicates.

        Returns:
        - bool -- True if there are duplicates in the list, otherwise False.
        """    
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(nums)) == len(nums):
            return False
        return True
    
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return False
            new_set.add(i)
        return True
    
# Input: nums = [1, 2, 3, 3]
# Output: true


# Input: nums = [1, 2, 3, 4]
# Output: false
