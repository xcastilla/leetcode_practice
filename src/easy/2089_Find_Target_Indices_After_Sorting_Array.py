"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/
Runtime: 48 ms, faster than 76.39% of Python3 online submissions for Find Target Indices After Sorting Array.
Memory Usage: 14.1 MB, less than 81.46% of Python3 online submissions for Find Target Indices After Sorting Array.
"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        l = bisect.bisect_left(nums, target)
        if l >= len(nums) or nums[l] != target:
            return []
        r = bisect.bisect_right(nums, target)
        return list(range(l,  r))
        