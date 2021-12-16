"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
Runtime: 912 ms, faster than 99.18% of Python3 online submissions for Find the Minimum and Maximum Number of Nodes Between Critical Points.
Memory Usage: 55.1 MB, less than 26.90% of Python3 online submissions for Find the Minimum and Maximum Number of Nodes Between Critical Points.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first, last = None, None
        mn, mx = None, None
        prev = head
        cur = head.next
        i = 1
        while cur.next:
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                if first is None:
                    first = i
                else:
                    mx = i - first
                    mn = i - first if last is None else min(mn, i - last)
                    last = i
                    
            prev = cur
            cur = cur.next
            i += 1

        if last is None:
            return [-1, -1]

        return [mn, mx]
            
        