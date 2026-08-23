class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left = right = 0
        qLeft = qRight = 0

        for i in range(half):
            if num[i] == '?':
                qLeft += 1
            else:
                left += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                qRight += 1
            else:
                right += int(num[i])

        return 2 * (left - right) + 9 * (qLeft - qRight) != 0