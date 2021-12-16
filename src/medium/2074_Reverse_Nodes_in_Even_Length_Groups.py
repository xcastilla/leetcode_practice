"""
https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
Runtime: 2280 ms, faster than 82.34% of Python3 online submissions for Reverse Nodes in Even Length Groups.
Memory Usage: 53.9 MB, less than 38.95% of Python3 online submissions for Reverse Nodes in Even Length Groups.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gl = 2
        s = []
        cur = head.next
        last = head
        while cur:
            read = 0
            while cur and read < gl:
                s.append(cur)
                read += 1
                cur = cur.next
            
            if read % 2 != 0:
                last.next = s[0]
                last = s[-1]
            else:
                # Reverse stack
                while len(s):
                    node = s.pop()
                    last.next = node
                    last = node
                    last.next = None
            s = []
            gl += 1
        
        return head
                
                
                
            
            
            
            
        