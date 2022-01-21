"""
https://leetcode.com/problems/minimum-moves-to-reach-target-score/
Runtime: 41 ms, faster than 62.19% of Python3 online submissions for Minimum Moves to Reach Target Score.
Memory Usage: 14.3 MB, less than 48.48% of Python3 online submissions for Minimum Moves to Reach Target Score.
"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ops = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0 and target:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            ops += 1
        if target > 1:
            ops += target - 1
        return ops