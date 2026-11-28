class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1

        total = [0] * (n + 1)
        for f in range(1, n + 1):
            s = 0
            for k in range(f, n + 1, f):
                s += cnt[k]
            total[f] = s

        m = min(p for _, p in items)
        cands = []
        for f, p in items:
            g = total[f] - 1
            if g > 0 and p < 2 * m:
                cands.append((p, g))
        cands.sort()

        rem = budget
        ans = 0
        for p, g in cands:
            u = min(g, rem // p)
            rem -= u * p
            ans += 2 * u
            if u < g:
                break

        ans += rem // m
        return ans