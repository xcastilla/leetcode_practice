"""
https://leetcode.com/problems/edit-distance/
Runtime: 184 ms, faster than 49.70% of Python3 online submissions for Edit Distance.
Memory Usage: 17.9 MB, less than 44.03% of Python3 online submissions for Edit Distance.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        for i in range(len(word1)):
            for j in range(len(word2)):
                # substitute or keep
                c1 = dp[i][j] if word1[i] == word2[j] else dp[i][j] + 1
                # remove
                c2 = dp[i][j +1] + 1
                # add
                c3 = dp[i + 1][j] + 1
                dp[i + 1][j + 1] = min(c1, c2, c3)

        return dp[-1][-1]
        