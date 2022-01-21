"""
https://leetcode.com/problems/two-furthest-houses-with-different-colors/submissions/
Runtime: 36 ms, faster than 91.85% of Python3 online submissions for Two Furthest Houses With Different Colors.
Memory Usage: 14.4 MB, less than 14.58% of Python3 online submissions for Two Furthest Houses With Different Colors.
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_d = 0
        f = {}
        for i in range(len(colors)):
            if colors[i] not in f:
                f[colors[i]] = i
            for k, v in f.items():
                max_d = max(max_d, i - v if k != colors[i] else 0)  
        return max_d


"""
Runtime: 36 ms, faster than 91.85% of Python3 online submissions for Two Furthest Houses With Different Colors.
Memory Usage: 14.3 MB, less than 14.58% of Python3 online submissions for Two Furthest Houses With Different Colors.
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i, j = 0, len(colors) - 1
        # find max distance from left and right
        while colors[i] == colors[j]:
            i += 1
        while colors[0] == colors[j]:
            j -= 1
        return max(len(colors)  - 1 - i, j)
        
        