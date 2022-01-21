"""
https://leetcode.com/problems/count-nodes-with-the-highest-score/
Runtime: 1432 ms, faster than 76.05% of Python3 online submissions for Count Nodes With the Highest Score.
Memory Usage: 130.2 MB, less than 31.10% of Python3 online submissions for Count Nodes With the Highest Score.
"""

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def rec_count(node, counts):
            sc = 0
            for son in tree[node]:
                sc += rec_count(son, counts)
            counts[node] = sc
            return sc + 1

        tree = defaultdict(list)
        for i, p in enumerate(parents):
            if p == -1:
                head = i
            tree[p].append(i)
        counts = [0] * len(parents)
        rec_count(head, counts)
        
        mx = 0
        ct_max = 0
        for n in range(len(parents)):
            score = 1
            for son in tree[n]:
                score *= counts[son] + 1
            score *= max(len(parents) - (counts[n] + 1), 1)
            if score > mx:
                mx = score
                ct_max = 1
            elif score == mx:
                ct_max += 1
        return ct_max
            
                
                
                
        
        
            
            
                
        
        
            
            
        
            
            
            
        