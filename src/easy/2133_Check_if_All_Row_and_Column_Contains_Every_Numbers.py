"""
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
Runtime: 986 ms, faster than 53.24% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
Memory Usage: 15.7 MB, less than 8.92% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
"""

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rows[i].add(matrix[i][j])
                cols[j].add(matrix[i][j])
        
        for i in range(len(matrix)):
            if i + 1 not in rows[0] or i + 1 not in cols[0]:
                return False
        
        ref_r = rows[0]
        ref_c = cols[0]
        for i in range(1, len(rows)):
            if ref_r != rows[i] or ref_c != cols[i]:
                return False
            
        return True
        
        
        