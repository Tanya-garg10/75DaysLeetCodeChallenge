
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for i in range(n):
            total = 0

            for j in range(i, min(i + r, n)):
                total += nums[j]
                length = j - i + 1

                if l <= length <= r and total > 0:
                    min_sum = min(min_sum, total)

        return min_sum if min_sum != float('inf') else -1
