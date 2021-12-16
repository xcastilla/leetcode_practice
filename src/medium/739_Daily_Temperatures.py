"""
https://leetcode.com/problems/daily-temperatures/submissions/
Runtime: 1232 ms, faster than 67.16% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.4 MB, less than 47.80% of Python3 online submissions for Daily Temperatures.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        q = []
        for i in range(0, len(temperatures)):
            while len(q) and temperatures[q[-1]] < temperatures[i]:
                el = q.pop()
                ans[el] = i - el
            q.append(i)
        return ans
            
        
        