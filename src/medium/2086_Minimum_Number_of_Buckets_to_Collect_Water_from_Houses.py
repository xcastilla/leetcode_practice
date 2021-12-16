"""
https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/
Runtime: 168 ms, faster than 36.14% of Python3 online submissions for Minimum Number of Buckets Required to Collect Rainwater from Houses.
Memory Usage: 15.8 MB, less than 33.68% of Python3 online submissions for Minimum Number of Buckets Required to Collect Rainwater from Houses.
"""

class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        total = 0
        for i, n in enumerate(street):
            if n == '.':
                if i - 1 >= 0 and street[i - 1] == 'H':
                    street[i - 1] = 'B'
                    total += 1
                    if i + 1 < len(street) and street[i + 1] == 'H':
                        street[i + 1] = 'B'
            if n == 'H':
                if (i - 1 < 0 or street[i - 1] != ".") and (i + 1 >= len(street) or street[i + 1] != "."):
                    return -1
                if i - 1 >= 0 and street[i - 1] == '.' and (i + 1 >= len(street) or street[i + 1] == 'H'):
                    total += 1
                    street[i] = 'B'

        return total



    
    
    
    
    
    
            
        
        
        