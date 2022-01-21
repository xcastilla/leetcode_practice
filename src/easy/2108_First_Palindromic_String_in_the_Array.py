"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array
Runtime: 100 ms, faster than 50.00% of Python3 online submissions for Find First Palindromic String in the Array.
Memory Usage: 14.4 MB, less than 83.33% of Python3 online submissions for Find First Palindromic String in the Array.
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isP(w):
            i, j = 0, len(w) - 1
            while i <= j:
                if w[i] != w[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for w in words:
            if isP(w): return w
        return ""
        