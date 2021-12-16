"""
https://leetcode.com/problems/coin-change/
Runtime: 1468 ms, faster than 56.90% of Python3 online submissions for Coin Change.
Memory Usage: 14.6 MB, less than 64.33% of Python3 online submissions for Coin Change.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1