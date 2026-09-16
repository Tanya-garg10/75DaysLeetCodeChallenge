class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        prev = [1] * (n + 1)
        
        for j in range(1, k + 1):
            curr = [0] * (n + 1)
            prefix = 0
            for i in range(1, n + 1):
                curr[i] = (curr[i - 1] + prefix) % MOD
                prefix = (prefix + prev[i]) % MOD
            prev = curr
        
        return prev[n]