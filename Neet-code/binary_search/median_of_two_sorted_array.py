def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)
    left, right = 0, n
    
    while left <= right:
        # Partition nums1 and nums2
        partition1 = (left + right) // 2
        partition2 = (n + m + 1) // 2 - partition1
        
        # Get the left and right elements for nums1
        maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        minRight1 = nums1[partition1] if partition1 < n else float('inf')
        
        # Get the left and right elements for nums2
        maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        minRight2 = nums2[partition2] if partition2 < m else float('inf')
        
        # Check if we have found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # If the total length is odd, return the maximum of the left parts
            if (n + m) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            # If the total length is even, return the average of the middle values
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        elif maxLeft1 > minRight2:
            # Too far right on nums1, move left
            right = partition1 - 1
        else:
            # Too far left on nums1, move right
            left = partition1 + 1
    
    raise ValueError("Input arrays are not sorted.")


nums1 = [1,3]
nums2 = [2,4]
print(findMedianSortedArrays(nums1, nums2)) 