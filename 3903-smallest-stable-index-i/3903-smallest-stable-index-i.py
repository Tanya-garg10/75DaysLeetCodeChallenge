class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        right_min = [0] * n
        right_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])

        left_max = nums[0]

        for i in range(n):
            left_max = max(left_max, nums[i])

            if left_max - right_min[i] <= k:
                return i

        return -1