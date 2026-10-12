from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        if isqrt(n) ** 2 == n:
            return 1

        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        for x in range(1, isqrt(n) + 1):
            r = n - x * x
            if isqrt(r) ** 2 == r:
                return 2

        return 3