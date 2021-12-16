"""
https://leetcode.com/problems/count-vowel-substrings-of-a-string/
Runtime: 88 ms, faster than 62.83% of Python3 online submissions for Count Vowel Substrings of a String.
Memory Usage: 14.1 MB, less than 79.32% of Python3 online submissions for Count Vowel Substrings of a String.
"""

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        start, end = 0, None
        d = {'a': 0, 'e':0, 'i': 0, 'o': 0, 'u': 0}
        count = 0
        while start < len(word):
            while start < len(word) and word[start] not in d:
                start += 1
            end = start
            left = 5
            d = {'a': 0, 'e':0, 'i': 0, 'o': 0, 'u': 0}
            while end < len(word) and word[end] in d:
                d[word[end]] += 1
                if d[word[end]] == 1:
                    left -= 1
                if left == 0:
                    count += 1
                end += 1
                
            if start < len(word):
                d[word[start]] -= 1
                if d[word[start]] == 0:
                    left += 1
                start += 1
        return count