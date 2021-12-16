"""
https://leetcode.com/problems/subsets
Runtime: 32 ms, faster than 83.17% of Python3 online submissions for Subsets.
Memory Usage: 14.4 MB, less than 52.69% of Python3 online submissions for Subsets.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(r):
            if len(r) == 0:
                return [[]]
            ret = helper(r[1:])
            res = []
            for sr in ret:
                res.append(sr)
                res.append([r[0]] + sr)
            return res
        
        return helper(nums)  