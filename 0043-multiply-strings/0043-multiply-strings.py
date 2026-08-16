class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                product = a * b

                pos1 = i + j
                pos2 = i + j + 1

                total = product + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        result = ""

        for digit in res:
            if result or digit != 0:
                result += str(digit)

        return result