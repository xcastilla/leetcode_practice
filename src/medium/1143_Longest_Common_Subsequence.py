"""
https://leetcode.com/problems/longest-common-subsequence/
Runtime: 484 ms, faster than 47.75% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22 MB, less than 79.01% of Python3 online submissions for Longest Common Subsequence.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                c1 = 1 + dp[i][j] if text1[i] == text2[j] else 0
                c2 = dp[i + 1][j]
                c3 = dp[i][j + 1]
                dp[i + 1][j + 1] = max(c1, c2, c3)
        return dp[-1][-1]