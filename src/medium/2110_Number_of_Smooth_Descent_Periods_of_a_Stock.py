"""
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock
Runtime: 1044 ms, faster than 77.67% of Python3 online submissions for Number of Smooth Descent Periods of a Stock.
Memory Usage: 28 MB, less than 70.55% of Python3 online submissions for Number of Smooth Descent Periods of a Stock.
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ret = 0
        i = 0
        while i < len(prices):
            last = prices[i]
            cl = 1
            for sz in range(1, len(prices) - i):
                if prices[i + sz] != last - 1:
                    break
                cl += 1
                last = prices[i + sz]
            ret += cl * (cl + 1) // 2
            i += cl
                
        return ret
                
        
        