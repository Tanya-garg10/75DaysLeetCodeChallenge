class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            best = float('inf')
            for d in (1, 2, 3):
                if j - d >= 0:
                    best = min(best, dp[j - d] + d * d)
            dp[j] = best + costs[j - 1]
        return dp[n]