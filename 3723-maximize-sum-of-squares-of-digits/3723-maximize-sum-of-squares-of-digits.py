class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        res = "9" * q
        if q < num:
            res += str(r)
            res += "0" * (num - q - 1)
        return res