class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        prev2 = 1  
        prev1 = 1  
        
        for i in range(2, n + 1):
            curr = 0
            one_digit = s[i - 1]
            two_digit = s[i - 2:i]
            
            if one_digit != '0':
                curr += prev1
            if '10' <= two_digit <= '26':
                curr += prev2
            
            prev2, prev1 = prev1, curr
        
        return prev1