"""
https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
Runtime: 956 ms, faster than 60.82% of Python3 online submissions for Removing Minimum and Maximum From Array.
Memory Usage: 27.6 MB, less than 83.20% of Python3 online submissions for Removing Minimum and Maximum From Array.
"""

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn_i, mx_i = 0, 0
        for i, n in enumerate(nums):
            if n < nums[mn_i]:
                mn_i = i
            if n > nums[mx_i]:
                mx_i = i
        return min(max(mn_i + 1, mx_i + 1),
                   max(len(nums) - mn_i, len(nums) - mx_i),
                   mx_i + 1 + len(nums) - mn_i,
                   mn_i + 1 + len(nums) - mx_i)
        
        
        
        
        
        
        
        