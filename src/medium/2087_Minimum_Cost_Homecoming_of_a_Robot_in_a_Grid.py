"""
https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
Runtime: 1644 ms, faster than 32.18% of Python3 online submissions for Minimum Cost Homecoming of a Robot in a Grid.
Memory Usage: 28.4 MB, less than 95.49% of Python3 online submissions for Minimum Cost Homecoming of a Robot in a Grid.
"""

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r_dir = 1 if homePos[0] > startPos[0] else -1
        c_dir = 1 if homePos[1] > startPos[1] else -1

        r, c = startPos
        distance = 0
        while (r, c) != tuple(homePos):
            next_col_cost = float('inf') if c == homePos[1] else colCosts[c + c_dir]
            while r != homePos[0] and rowCosts[r + r_dir] <= next_col_cost:
                distance += rowCosts[r + r_dir]
                r = r + r_dir
            next_row_cost = float('inf') if r == homePos[0] else rowCosts[r + r_dir]
            while c != homePos[1] and colCosts[c + c_dir] <= next_row_cost:
                distance += colCosts[c + c_dir]
                c = c + c_dir
                
        return distance
            
                    
                

            
        
        