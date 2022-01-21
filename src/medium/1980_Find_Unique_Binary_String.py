"""
https://leetcode.com/problems/find-unique-binary-string/
Runtime: 41 ms, faster than 35.69% of Python3 online submissions for Find Unique Binary String.
Memory Usage: 14.4 MB, less than 38.91% of Python3 online submissions for Find Unique Binary String.
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        r = ""
        for i in range(len(nums)):
            r += "1" if nums[i][i] == "0" else "0"
        return r


"""
Runtime: 46 ms, faster than 31.67% of Python3 online submissions for Find Unique Binary String.
Memory Usage: 14.5 MB, less than 22.67% of Python3 online submissions for Find Unique Binary String.
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def helper(p, acc):
            if p == 0:
                if acc not in s:
                    return acc
                return None
            
            r = helper(p - 1, acc + "0")
            if r: return r
            r = helper(p - 1, acc + "1")
            return r
        
        s = set(nums)
        return helper(len(nums[0]), "")
