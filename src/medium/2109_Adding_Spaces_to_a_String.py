"""
https://leetcode.com/problems/adding-spaces-to-a-string
Runtime: 652 ms, faster than 100.00% of Python3 online submissions for Adding Spaces to a String.
Memory Usage: 51.6 MB, less than 16.67% of Python3 online submissions for Adding Spaces to a String.
"""

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        o = ""
        ct = 0
        for sp in spaces:
            o += s[ct:sp]
            o += " "
            ct = sp
        o += s[ct:]
        return o
            
        