"""
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
Runtime: 52 ms, faster than 83.33% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
Memory Usage: 15.2 MB, less than 19.66% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        @lru_cache(None)
        def count(i, acc):
            if acc == bor:
                return 2**(len(nums) - i)
            if i >= len(nums):
                return 0
            return count(i + 1, acc | nums[i]) + count(i + 1, acc)
        bor = reduce(lambda a,b: a | b, nums)
        return count(0, 0)


"""
Runtime: 48 ms, faster than 85.21% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
Memory Usage: 15.4 MB, less than 18.35% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        @lru_cache(None)
        def count(i, acc):
            if i >= len(nums):
                if acc == bor:
                    return 1
                return 0

            return count(i + 1, acc | nums[i]) + count(i + 1, acc)
        bor = functools.reduce(lambda a,b: a | b, nums)
        return count(0, 0)