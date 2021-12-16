"""
https://leetcode.com/problems/count-common-words-with-one-occurrence/
Runtime: 64 ms, faster than 91.35% of Python3 online submissions for Count Common Words With One Occurrence.
Memory Usage: 14.7 MB, less than 72.39% of Python3 online submissions for Count Common Words With One Occurrence.
"""

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d = defaultdict(int)
        for w in words1:
            d[w] += 1

        # Remove keys with values > 1. Can't do it while iterating through items
        ignore = []
        for k, v in d.items():
            if v > 1:
                ignore.append(k)
        for k in ignore:
            d.pop(k)

        # Decrease only words already existing in d
        for w in words2:
            if w in d:
                d[w] -= 1
        ct = 0
        for v in d.values():
            if v == 0:
                ct += 1
        return ct
        