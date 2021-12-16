"""
https://leetcode.com/problems/is-subsequence
Runtime: 20 ms, faster than 99.48% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.4 MB, less than 24.69% of Python3 online submissions for Is Subsequence.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt1 = 0
        pt2 = 0
        while pt1 < len(s) and pt2 < len(t):
            if t[pt2] == s[pt1]:
                pt1 += 1
            pt2 += 1
        
        return pt1 == len(s)