"""
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
Runtime: 1632 ms, faster than 51.60% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.
Memory Usage: 49.6 MB, less than 20.21% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        nums = sorted(nums)
        d = nums[0] % x
        for i in range(1, len(nums)):
            if nums[i] % x != d:
                return -1
            
        tgt = nums[len(nums) // 2]
        ops = 0
        for i in range(len(nums)):
            ops += abs(nums[i] - tgt) // x
        return ops