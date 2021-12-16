"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/
Runtime: 60 ms, faster than 97.44% of Python3 online submissions for Kth Distinct String in an Array.
Memory Usage: 14.7 MB, less than 27.86% of Python3 online submissions for Kth Distinct String in an Array.
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        ignore = set()
        for i, n in enumerate(arr):
            if n in d:
                ignore.add(n)
            else:
                d[n] = True
        
        ct = 0
        for i in range(len(arr)):
            if arr[i] not in ignore:
                ct += 1
                if ct == k:
                    return arr[i]
        
        return ""
        