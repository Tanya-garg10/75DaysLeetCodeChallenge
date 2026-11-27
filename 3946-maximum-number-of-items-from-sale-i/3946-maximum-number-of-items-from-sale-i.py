class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        NEG = float('-inf')
        dp = [0] * (budget + 1)  
        
        for i in range(n):
            f, p = items[i]
            g = 0
            for j in range(n):
                if j != i and items[j][0] % f == 0:
                    g += 1
            u = [NEG] * (budget + 1)
            for b in range(p, budget + 1):
                best = dp[b - p] + g + 1
                if u[b - p] != NEG and u[b - p] + 1 > best:
                    best = u[b - p] + 1
                u[b] = best
            for b in range(budget + 1):
                if u[b] > dp[b]:
                    dp[b] = u[b]

        return dp[budget]