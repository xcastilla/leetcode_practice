"""
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks
Runtime: 151 ms, faster than 85.00% of Python3 online submissions for Minimum Number of Work Sessions to Finish the Tasks.
Memory Usage: 16.9 MB, less than 53.50% of Python3 online submissions for Minimum Number of Work Sessions to Finish the Tasks.
"""

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        @cache
        def helper(tasks, rem):
            if len(tasks) == 0:
                return 1
            elif rem < tasks[0]:
                return 1 + helper(tasks, sessionTime)
            minimum = float('inf')
            for j in range(len(tasks)):
                if tasks[j] > rem: break
                ret = helper(tasks[:j] + tasks[j+1:], rem - tasks[j])
                minimum = min(minimum, ret)
            return minimum
                    
        tasks.sort()
        return helper(tuple(tasks), sessionTime)
            
            
            
        
        
                
                
        
                        
                    
        
        
                            
                            
                    
                
                
        
        
            
        
            
            
        