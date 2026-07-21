class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"

        original_ones = s.count('1')

        types = []
        lengths = []

        for ch in t:
            if not types or types[-1] != ch:
                types.append(ch)
                lengths.append(1)
            else:
                lengths[-1] += 1

        ans = original_ones

        for i in range(1, len(types) - 1):
            if types[i] == '1' and types[i - 1] == '0' and types[i + 1] == '0':
                ans = max(ans, original_ones + lengths[i - 1] + lengths[i + 1])

        return ans