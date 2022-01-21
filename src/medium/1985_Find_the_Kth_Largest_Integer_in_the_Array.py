"""
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
Runtime: 256 ms, faster than 87.48% of Python3 online submissions for Find the Kth Largest Integer in the Array.
Memory Usage: 22.7 MB, less than 90.26% of Python3 online submissions for Find the Kth Largest Integer in the Array.
"""

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key = lambda x: int(x), reverse=True)
        return nums[k - 1]