"""
https://leetcode.com/problems/plates-between-candles/
Runtime: 2140 ms, faster than 43.69% of Python3 online submissions for Plates Between Candles.
Memory Usage: 53.9 MB, less than 52.51% of Python3 online submissions for Plates Between Candles.
"""

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ends = []
        acc = []
        ct_new = 0
        ct_old = 0
        for i in range(len(s)):
            if s[i] == '|':
                ends.append(i)
                ct_old += ct_new
                acc.append(ct_old)
                ct_new = 0
            else:
                ct_new += 1
                acc.append(ct_old)         
                
        ret = []
        for q in queries:
            left = bisect.bisect_left(ends, q[0])
            right = bisect.bisect_right(ends, q[1])
            if left >= right - 1 or left >= len(s) or right >= len(s):
                ret.append(0)
                continue
            ret.append(acc[ends[right-1]] - acc[ends[left]])

        return ret
        
            
        
        
        
                
            
            
        
        
        
        
        
        
        
        
        
        