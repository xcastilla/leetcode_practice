"""
Runtime: 6031 ms, faster than 12.07% of Python3 online submissions for Sum of Subarray Ranges.
Memory Usage: 14 MB, less than 99.28% of Python3 online submissions for Sum of Subarray Ranges.
"""
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        tot = 0
        for i in range(len(nums)):
            mx = mn = nums[i]
            for j in range(i + 1, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                tot += mx - mn
        return tot


"""
Runtime: 8889 ms, faster than 5.04% of Python3 online submissions for Sum of Subarray Ranges.
Memory Usage: 14.4 MB, less than 77.52% of Python3 online submissions for Sum of Subarray Ranges.
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        tot = 0
        q = [(n, n) for n in nums]
        while len(q) > 1:
            new_q = []
            for i in range(len(q) - 1):
                mn = min(q[i][1], q[i + 1][1])
                mx = max(q[i][0], q[i + 1][0])
                tot += mx - mn
                new_q.append((mx, mn))
            q = new_q
        return tot
