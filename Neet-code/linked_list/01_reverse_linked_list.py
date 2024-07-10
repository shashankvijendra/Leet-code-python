"""Reverse a Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

nums = [0,1,2,3]
n = 0
curr = ListNode(0)
head = curr
while n<len(nums):
    while curr.next:
        curr = curr.next
    curr.next = ListNode(nums[n])
    n+=1
    
Solution().reverseList(curr)

# Input: head = [0,1,2,3]
# Output: [3,2,1,0]


# Input: head = []
# Output: []
