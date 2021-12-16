"""
https://leetcode.com/problems/decode-the-slanted-ciphertext
Runtime: 584 ms, faster than 75.74% of Python3 online submissions for Decode the Slanted Ciphertext.
Memory Usage: 35.2 MB, less than 26.55% of Python3 online submissions for Decode the Slanted Ciphertext.
"""

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if len(encodedText) == 0:
            return ""
        cols = len(encodedText) // rows
        ciph = []
        sj = 0
        while sj < cols:
            i, j = 0, sj
            new_line = ""
            while i < rows and j < cols:
                new_line += encodedText[i * cols + j]
                i += 1
                j += 1
            ciph.append(new_line)
            sj += 1
                
        # remove empty words from the back
        j = len(ciph) - 1
        while len(ciph[j].strip()) == 0:
            j -= 1
        ciph = ciph[:j+1]
        
        # remove spaces from last word
        ciph = ''.join(ciph)
        j = len(ciph) - 1
        while ciph[j] == " ":
            j -= 1
        ciph = ciph[: j + 1]
        
        return ciph
        
        