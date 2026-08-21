from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        cur_lcm = lcm(cur_lcm, coins[i])
                        bits += 1

                        if cur_lcm > x:
                            valid = False
                            break

                if valid:
                    if bits % 2:
                        total += x // cur_lcm
                    else:
                        total -= x // cur_lcm

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left