"""
https://leetcode.com/problems/find-all-people-with-secret
Runtime: 2104 ms, faster than 92.44% of Python3 online submissions for Find All People With Secret.
Memory Usage: 44.5 MB, less than 91.23% of Python3 online submissions for Find All People With Secret.
"""

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings, key = lambda x: x[2])
        secret = [False] * n
        secret[0] = True
        secret[firstPerson] = True
        idx = 0
        res = set([0, firstPerson])
        while idx < len(meetings):
            t = meetings[idx][2]
            next_meetings = []
            # we need to consider all meetings at time t at once
            while idx < len(meetings) and meetings[idx][2] == t:
                next_meetings.append(meetings[idx])
                if secret[meetings[idx][0]] or secret[meetings[idx][1]]:
                    secret[meetings[idx][0]] = secret[meetings[idx][1]] = True
                idx += 1
            # go through all meetings again forward and backwards
            for i in range(len(next_meetings) -1 , -1, -1):
                next_m = next_meetings[i]
                if secret[next_m[0]] or secret[next_m[1]]:
                    secret[next_m[0]] = secret[next_m[1]] = True
                    res.add(next_m[0])
                    res.add(next_m[1])
            for i in range(len(next_meetings)):
                next_m = next_meetings[i]
                if secret[next_m[0]] or secret[next_m[1]]:
                    secret[next_m[0]] = secret[next_m[1]] = True
                    res.add(next_m[0])
                    res.add(next_m[1])
        return list(res)
                
                
            
            
        
        