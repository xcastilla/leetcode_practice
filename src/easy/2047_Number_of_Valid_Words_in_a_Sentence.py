"""
https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
Runtime: 28 ms, faster than 99.72% of Python3 online submissions for Number of Valid Words in a Sentence.
Memory Usage: 14.5 MB, less than 33.95% of Python3 online submissions for Number of Valid Words in a Sentence.
"""

class Solution:
    def countValidWords(self, sentence: str) -> int:
        ret = 0
        for w in sentence.split(' '):
            if w == "":
                continue
            flag = True
            c_s = 0
            for i, c in enumerate(w):
                if c in '_!.,':
                    if i != len(w) - 1:
                        flag = False
                        break
                elif c == '-':
                    c_s += 1
                    if c_s > 1 or i - 1 < 0 or i + 1 >= len(w) or not str.islower(w[i - 1]) or not str.islower(w[i + 1]):
                        flag = False
                        break
                elif not str.islower(c):
                    flag = False
                    break
            if flag:
                ret += 1
        return ret
                
                
        
        