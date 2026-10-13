class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted((x * x for x in nums), reverse=True)
        add = (len(sq) + 1) // 2
        return sum(sq[:add]) - sum(sq[add:])