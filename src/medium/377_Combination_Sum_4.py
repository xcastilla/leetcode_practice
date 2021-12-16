"""
https://leetcode.com/problems/combination-sum-iv/
Runtime: 40 ms, faster than 73.68% of Python3 online submissions for Combination Sum IV.
Memory Usage: 14.3 MB, less than 47.16% of Python3 online submissions for Combination Sum IV.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        nums = sorted(nums)
        for i in range(1, target + 1):
            for c in nums:
                if i - c < 0: break
                dp[i] += dp[i - c]
                    
        return dp[-1]

