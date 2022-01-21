"""
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
Runtime: 32 ms, faster than 61.06% of Python3 online submissions for Check if Numbers Are Ascending in a Sentence.
Memory Usage: 14.2 MB, less than 78.64% of Python3 online submissions for Check if Numbers Are Ascending in a Sentence.
"""

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = float('-inf')
        for n in s.split(' '):
            if n.isnumeric():
                if int(n) <= last:
                    return False
                last = int(n)
        return True

        