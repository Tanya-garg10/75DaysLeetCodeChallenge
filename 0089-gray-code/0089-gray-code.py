class Solution:
    def grayCode(self, n):
        result = [0]

        for i in range(n):
            for num in reversed(result):
                result.append(num | (1 << i))

        return result