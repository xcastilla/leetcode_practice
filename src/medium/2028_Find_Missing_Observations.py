"""
https://leetcode.com/problems/find-missing-observations/
Runtime: 1657 ms, faster than 46.39% of Python3 online submissions for Find Missing Observations.
Memory Usage: 26.2 MB, less than 6.70% of Python3 online submissions for Find Missing Observations.
"""

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:        
        n_sum = (mean * (len(rolls) + n)) - sum(rolls)
        if n_sum > 6 * n or n_sum < n:
            return []
        
        flr, m = divmod(n_sum, n)
        return [flr] * (n - m) + [flr + 1] * m