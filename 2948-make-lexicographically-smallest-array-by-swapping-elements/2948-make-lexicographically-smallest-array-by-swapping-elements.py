class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        pairs = sorted((nums[i], i) for i in range(n))

        ans = [0] * n

        start = 0

        while start < n:
            end = start

            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            values = [pairs[i][0] for i in range(start, end + 1)]

            indices = sorted(pairs[i][1] for i in range(start, end + 1))

            for value, index in zip(values, indices):
                ans[index] = value

            start = end + 1

        return ans