class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        result = 0
        
        for i in range(31, -1, -1):
            if (b << i) <= a:
                a -= (b << i)
                result += (1 << i)
        
        if negative:
            result = -result
        
        return result