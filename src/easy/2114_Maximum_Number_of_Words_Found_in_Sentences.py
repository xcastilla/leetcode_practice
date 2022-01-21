"""
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences
Runtime: 44 ms, faster than 60.65% of Python3 online submissions for Maximum Number of Words Found in Sentences.
Memory Usage: 14.4 MB, less than 42.02% of Python3 online submissions for Maximum Number of Words Found in Sentences.
"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split(" ")) for s in sentences])