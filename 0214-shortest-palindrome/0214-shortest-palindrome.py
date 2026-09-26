class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev_s = s[::-1]
        combined = s + '#' + rev_s
        n = len(combined)
        
        fail = [0] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = fail[j - 1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j
        
        L = fail[n - 1]  
        
        return rev_s[:len(s) - L] + s