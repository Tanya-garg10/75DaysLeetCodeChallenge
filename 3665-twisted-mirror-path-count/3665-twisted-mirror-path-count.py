class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)] 
        D = [[0] * (n + 1) for _ in range(m + 1)]  
        total_start = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    r_in, d_in = 0, 0
                    ways = total_start
                    R[i][j + 1] = (R[i][j + 1] + ways) % MOD
                    D[i + 1][j] = (D[i + 1][j] + ways) % MOD
                    continue
                r_in, d_in = R[i][j], D[i][j]
                if grid[i][j] == 0:
                    ways = (r_in + d_in) % MOD
                    if ways:
                        R[i][j + 1] = (R[i][j + 1] + ways) % MOD
                        D[i + 1][j] = (D[i + 1][j] + ways) % MOD
                else:
                    D[i + 1][j] = (D[i + 1][j] + r_in) % MOD
                    R[i][j + 1] = (R[i][j + 1] + d_in) % MOD

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD