"""
https://leetcode.com/problems/time-needed-to-buy-tickets/submissions/
Runtime: 43 ms, faster than 63.94% of Python3 online submissions for Time Needed to Buy Tickets.
Memory Usage: 14.2 MB, less than 79.54% of Python3 online submissions for Time Needed to Buy Tickets.
"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tot = tickets[k]
        for i in range(len(tickets)):
            if i < k:
                tot += min(tickets[i], tickets[k])
            elif i > k:
                tot += min(tickets[i], tickets[k] - 1)
        return tot