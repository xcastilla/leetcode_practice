"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs
Runtime: 24 ms, faster than 90.00% of Python3 online submissions for Check if All A's Appears Before All B's.
Memory Usage: 14.2 MB, less than 80.00% of Python3 online submissions for Check if All A's Appears Before All B's.
"""

class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for c in s:
            if c == 'b':
                b = True
            elif b and c == 'a':
                return False
        return True