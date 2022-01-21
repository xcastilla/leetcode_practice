"""
https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid
Runtime: 1900 ms, faster than 48.52% of Python3 online submissions for Execution of All Suffix Instructions Staying in a Grid.
Memory Usage: 14.3 MB, less than 67.92% of Python3 online submissions for Execution of All Suffix Instructions Staying in a Grid.
"""

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ret = []
        mov = { 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0) }
        for i in range(len(s)):
            x, y = startPos
            j = i
            while j < len(s):
                x += mov[s[j]][0]
                y += mov[s[j]][1]
                if not (y >= 0 and y < n and x >= 0 and x < n):
                    break
                j += 1
            ret.append(j - i)
        return ret