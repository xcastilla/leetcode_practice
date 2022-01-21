"""
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores
Runtime: 100 ms, faster than 71.56% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
Memory Usage: 14.4 MB, less than 60.55% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
"""

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        min_dif = float('inf')
        for i in range(0, len(nums) - k + 1):
            min_dif = min(min_dif, nums[i] - nums[i + k - 1])
        return min_dif