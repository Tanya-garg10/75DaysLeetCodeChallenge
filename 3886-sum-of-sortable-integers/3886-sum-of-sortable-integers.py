class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                block = nums[s:s + k]
                desc = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        desc += 1
                if desc > 1:
                    ok = False
                    break
                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)
            if ok:
                total += k
        return total