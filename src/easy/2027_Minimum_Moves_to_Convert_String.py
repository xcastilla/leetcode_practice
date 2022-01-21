"""
https://leetcode.com/problems/minimum-moves-to-convert-string/
Runtime: 32 ms, faster than 65.10% of Python3 online submissions for Minimum Moves to Convert String.
Memory Usage: 14.1 MB, less than 76.12% of Python3 online submissions for Minimum Moves to Convert String.
"""

class Solution:
    def minimumMoves(self, s: str) -> int:
        i = ops = 0
        while i < len(s):
            if s[i] == 'X':
                ops += 1
                i += 3
            else:
                i += 1
        return ops