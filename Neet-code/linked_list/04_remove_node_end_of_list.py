"""Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list."""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solutions:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solutionss:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        data = head
        d = 0
        while data:
            data = data.next
            d+=1
        a = d-n
        if not a and d<=1:
            head = None
            return head
        elif not a:
            return head.next
        main = head
        while main and a>1:
            main = main.next
            a -= 1
        main.next = main.next.next
        return head or []
    
####Soluttion Provided in neetcode #####

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next


head = ListNode(1)

print(Solution().removeNthFromEnd(head=head, n=1))