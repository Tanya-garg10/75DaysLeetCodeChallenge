class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def f(b):
            return b * costBoth + max(0, need1 - b) * cost1 + max(0, need2 - b) * cost2

        return min(f(0), f(min(need1, need2)), f(max(need1, need2)))