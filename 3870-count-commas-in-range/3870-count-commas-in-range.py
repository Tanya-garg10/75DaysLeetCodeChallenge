class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        digits = 1
        lower = 1  
        while lower <= n:
            upper = lower * 10 - 1  
            upper = min(upper, n)
            count = upper - lower + 1
            commas_per_number = (digits - 1) // 3
            total += count * commas_per_number
            digits += 1
            lower *= 10
        return total