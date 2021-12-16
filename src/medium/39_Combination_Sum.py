"""
https://leetcode.com/problems/combination-sum/
Runtime: 64 ms, faster than 82.69% of Python3 online submissions for Combination Sum.
Memory Usage: 14.7 MB, less than 8.98% of Python3 online submissions for Combination Sum.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        candidates = sorted(candidates)
        for c in candidates:
            for i in range(c, target + 1):
                if i - c < 0: continue
                for sl in dp[i - c]:
                    dp[i].append(sl + [c])
        return dp[-1]


# Recursive approach with caching, slower but better memory usage
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates, target, [])
           
    def helper(self, candidates: List[int], target: int, acc: List[int]) -> List[List[int]]:
        if target == 0:
            return [sorted(acc)]
        if target < candidates[0]:
            return
        ret = []
        for candidate in candidates:
            if candidate <= target:
                sub_ret = self.helper(candidates, target - candidate, acc + [candidate])
                if not sub_ret:
                    continue
                for s in sub_ret:
                    if s and s not in ret:
                        ret.append(s)
                
        return ret