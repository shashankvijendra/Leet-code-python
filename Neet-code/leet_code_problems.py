

### 1. Longest Substring Without Repeating Characters

# Given a string `s`, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s):
    char_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(char_map[s[right]] + 1, left)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test the function
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3 (substring "abc")


### 2. Find the Duplicate Number


#Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return the duplicate number.

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Test the function
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2


### 3. Coin Change


# You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test the function
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)


### 4. Group Anagrams
# Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    
    return list(anagrams.values())

# Test the function
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


### 5. Kth Largest Element in an Array


# Find the `k`-th largest element in an unsorted array. Note that it is the `k`-th largest element in sorted order, not the `k`-th distinct element.

import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Test the function
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  # Output: 5



### 6. Merge Intervals

# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Test the function
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]


### 7. Product of Array Except Self

# Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

def product_except_self(nums):
    length = len(nums)
    output = [1] * length

    prefix = 1
    for i in range(length):
        output[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(length - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output

# Test the function
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]


### 8. Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []

    result, queue = [], deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Test the function with an example tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(level_order(root))  # Output: [[3], [9, 20], [15, 7]]

### 9. Combination Sum
# Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.
def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    backtrack(0, target, [])
    return result

# Test the function
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))  # Output: [[2, 2, 3], [7]]

### 10. Subarray Sum Equals K

# Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.
def subarray_sum(nums, k):
    count, cum_sum = 0, 0
    sum_map = {0: 1}

    for num in nums:
        cum_sum += num
        if cum_sum - k in sum_map:
            count += sum_map[cum_sum - k]
        sum_map[cum_sum] = sum_map.get(cum_sum, 0) + 1

    return count

# Test the function
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output: 2


### 11. Rotate Image

# You are given an `n x n` 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix)
print(matrix)
# Output: [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]

### 12. Word Break
# Given a string `s` and a dictionary of words `word_dict`, return true if `s` can be segmented into a space-separated sequence of one or more dictionary words.
def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[-1]

# Test the function
s = "leetcode"
word_dict = {"leet", "code"}
print(word_break(s, word_dict))  # Output: True

### 13. Palindrome Partitioning
# Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

def palindrome_partitioning(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])

    result = []
    backtrack(0, [])
    return result

# Test the function
s = "aab"
print(palindrome_partitioning(s))
# Output: [["a", "a", "b"], ["aa", "b"]]

### 14. Maximum Subarray

# Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6 (subarray [4,-1,2,1])

### 15. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index. You may imagine that `nums[-1]` and `nums[n]` are both `-∞`.

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Test the function
nums = [1,2,3,1]
print(find_peak_element(nums))  # Output: 2 (element 3)



# Question: Find Unique Pairs with a Minimum Difference
# Given an array of integers, find all unique pairs (a, b) where:

# a appears before b in the original list.

# The absolute difference between a and b is greater than or equal to a given target value.

# Duplicate values in the list are allowed, meaning the same number can be paired multiple times if it appears more than once in the list.


def find_valid_pairs(arr, target):
    arr.sort()  # Sort the array (preserves duplicates)
    valid_pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[j] - arr[i]) >= target:
                valid_pairs.append((arr[i], arr[j]))

    return valid_pairs

# Example Usage
arr = [1, 5, 3, 9, 7, 2, 8, 6, 5, 3]
target = 3
print(find_valid_pairs(arr))
#Output
# [(1, 5), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), 
#  (2, 5), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
#  (3, 6), (3, 7), (3, 8), (3, 9), (3, 6), (3, 7), (3, 8), (3, 9), 
#  (5, 9), (5, 8), (5, 7), (5, 6), (5, 9), (5, 8), (5, 7), (5, 6),
#  (6, 9), (6, 8), (6, 7), (7, 9)]



