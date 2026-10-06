class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        unmatched_close = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else: 
                if balance > 0:
                    balance -= 1
                else:
                    unmatched_close += 1
        
        return balance + unmatched_close