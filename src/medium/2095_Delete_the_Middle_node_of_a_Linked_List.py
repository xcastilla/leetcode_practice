"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Runtime: 1820 ms, faster than 14.29% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 60.9 MB, less than 100.00% of Python3 online submissions for Delete the Middle Node of a Linked List.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        prev, mid, cur = head, head, head
        while cur and cur.next:
            prev = mid
            mid = mid.next
            cur = cur.next.next
        prev.next = mid.next
        return head




            
        
        