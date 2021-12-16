"""
https://leetcode.com/problems/k-radius-subarray-averages/
Runtime: 1836 ms, faster than 65.51% of Python3 online submissions for K Radius Subarray Averages.
Memory Usage: 32.7 MB, less than 67.21% of Python3 online submissions for K Radius Subarray Averages.
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # We don't have enough elements to account for the whole window
        if len(nums) < (2 * k + 1):
            return [-1] * len(nums)
        # Array starts with radius -1 elements
        arr = [-1] * k

        # Initial window
        avg = 0
        for i in range(2*k + 1):
            avg += nums[i]

        c = k
        while c < len(nums):
            if c + k >= len(nums):
                arr.append(-1)
                c += 1
            else:
                arr.append(avg // (2 * k + 1))
                # Remove element left of the window
                avg -= nums[c - k]
                c += 1
                # Add element right or the window (or nothing if we went over)
                avg += nums[c + k] if c + k < len(nums) else 0
        return arr