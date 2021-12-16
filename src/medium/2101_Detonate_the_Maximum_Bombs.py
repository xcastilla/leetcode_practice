
"""
https://leetcode.com/problems/detonate-the-maximum-bombs/submissions/
Runtime: 753 ms, faster than 84.11% of Python3 online submissions for Detonate the Maximum Bombs.
Memory Usage: 14.8 MB, less than 55.41% of Python3 online submissions for Detonate the Maximum Bombs.
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def affects(b1, b2):
            return math.sqrt(math.pow(b1[0] - b2[0], 2) + math.pow(b1[1] - b2[1], 2)) <= b1[2]
        
        def explore(b, exploded):
            it = []
            ret = 1
            for b2 in d[b]:
                if not exploded[b2]:
                    it.append(b2)
                    exploded[b2] = True
            for b2 in it:
                ret += explore(b2, exploded)
                
            return ret
        
        d = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                if affects(bombs[i], bombs[j]):
                    d[i].append(j)
                if affects(bombs[j], bombs[i]):
                    d[j].append(i)
                
        self.mx = 0
        for i in range(len(bombs)):
            exploded = [False] * len(bombs)
            exploded[i] = True
            self.mx = max(self.mx, explore(i, exploded))
        return self.mx
        
        
        
        
    
                
                
        
        