"""
https://leetcode.com/problems/rings-and-rods/
Runtime: 28 ms, faster than 88.24% of Python3 online submissions for Rings and Rods.
Memory Usage: 14.2 MB, less than 78.89% of Python3 online submissions for Rings and Rods.
"""

class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        rs = set()
        for i in range(0, len(rings), 2):
            c = rings[i]
            r = rings[i + 1]
            d[r].add(c)
            if r not in rs and len(d[r]) == 3:
                rs.add(r)
        return len(rs)
            
        