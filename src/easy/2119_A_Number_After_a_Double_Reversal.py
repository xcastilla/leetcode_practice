"""
https://leetcode.com/problems/a-number-after-a-double-reversal/
Runtime: 19 ms, faster than 99.51% of Python3 online submissions for A Number After a Double Reversal.
Memory Usage: 14.1 MB, less than 90.15% of Python3 online submissions for A Number After a Double Reversal.
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return not num or num % 10 != 0