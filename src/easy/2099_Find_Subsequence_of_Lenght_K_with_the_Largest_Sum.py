"""
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
Runtime: 52 ms, faster than 100.00% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
Memory Usage: 14.8 MB, less than 20.00% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
"""

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        q = []
        for i, n in enumerate(nums):
            if len(q) < k:
                heapq.heappush(q, (n, i))
            else:
                heapq.heappushpop(q, (n, i))
        return [nums[v[1]] for v in sorted(q, key=lambda x: x[1])]