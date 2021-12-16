"""
https://leetcode.com/problems/coin-change-2/submissions/
Runtime: 244 ms, faster than 53.10% of Python3 online submissions for Coin Change 2.
Memory Usage: 14.4 MB, less than 69.58% of Python3 online submissions for Coin Change 2.
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]