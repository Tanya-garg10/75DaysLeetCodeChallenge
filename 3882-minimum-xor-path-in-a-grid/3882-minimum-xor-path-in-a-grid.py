class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reach = [[set() for _ in range(n)] for _ in range(m)]
        reach[0][0] = {grid[0][0]}

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j]
                prev = set()
                if i > 0:
                    prev |= reach[i - 1][j]
                if j > 0:
                    prev |= reach[i][j - 1]
                reach[i][j] = {x ^ v for x in prev}

        return min(reach[m - 1][n - 1])