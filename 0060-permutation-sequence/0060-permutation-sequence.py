class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        ans = []

        fact = 1
        for i in range(1, n):
            fact *= i

        for i in range(n, 0, -1):
            index = k // fact
            ans.append(nums.pop(index))
            k %= fact

            if i > 1:
                fact //= i - 1

        return ''.join(ans)