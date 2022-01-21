"""
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid
Runtime: 319 ms, faster than 41.26% of Python3 online submissions for Check if a Parentheses String Can Be Valid.
Memory Usage: 15.4 MB, less than 37.12% of Python3 online submissions for Check if a Parentheses String Can Be Valid.
"""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0: return False
        op = 0
        # Check balance of opening (
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0': op +=1
            else: op -= 1
            if op < 0: return False
        
        cl = 0
        # Check balance of closing )
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0': cl += 1
            else: cl -= 1
            if cl < 0: return False
        return True