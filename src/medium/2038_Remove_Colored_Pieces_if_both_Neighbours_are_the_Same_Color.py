"""
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color
Runtime: 220 ms, faster than 74.84% of Python3 online submissions for Remove Colored Pieces if Both Neighbors are the Same Color.
Memory Usage: 15.1 MB, less than 41.30% of Python3 online submissions for Remove Colored Pieces if Both Neighbors are the Same Color.
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c_idx = 0
        alice = 0
        bob = 0
        N = len(colors) - 1
        for i in range(1, len(colors)):
            if colors[i] == colors[c_idx]:
                if i - c_idx + 1 >= 3:
                    if colors[c_idx] == 'A': alice += 1
                    else: bob += 1
            else:
                c_idx = i
        if alice == 0 or bob >= alice:
            return False
        return True