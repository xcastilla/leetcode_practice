"""
https://leetcode.com/problems/minimum-operations-to-convert-number/
Runtime: 1232 ms, faster than 95.11% of Python3 online submissions for Minimum Operations to Convert Number.
Memory Usage: 14.4 MB, less than 84.54% of Python3 online submissions for Minimum Operations to Convert Number.
"""

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = [start]
        depth = 0
        seen = {}
        while len(q):
            new_q = []
            while len(q):
                el = q.pop()
                for n in nums:
                    sm = el + n
                    sb = el - n
                    xor = el ^ n
                    if sm == goal or sb == goal or xor == goal:
                        return depth + 1
                    if 0 <= sm <= 1000 and sm not in seen:
                        seen[sm] = True
                        new_q.append(sm)
                    if 0 <= sb <= 1000 and sb not in seen:
                        seen[sb] = True
                        new_q.append(sb)
                    if 0 <= xor <= 1000 and xor not in seen:
                        seen[xor] = True
                        new_q.append(xor)
            q = new_q
            depth += 1
        return -1
                        
                
                
            
        
        
        
        