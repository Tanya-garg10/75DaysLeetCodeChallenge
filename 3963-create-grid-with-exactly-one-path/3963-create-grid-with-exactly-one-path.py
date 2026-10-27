class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = ["." * n]
        for _ in range(m - 1):
            grid.append("#" * (n - 1) + ".")
        return grid