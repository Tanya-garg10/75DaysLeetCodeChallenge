class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        INF = float('inf')

        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m_sz = len(vals)
        cnt = [0] * (m_sz + 1)
        sm = [0] * (m_sz + 1)
        LOG = 1
        while (1 << LOG) <= m_sz:
            LOG += 1

        def upd(i, dc, ds):
            while i <= m_sz:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        def pref(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        def kth(kk):  
            pos = 0
            for b in range(LOG, -1, -1):
                nxt = pos + (1 << b)
                if nxt <= m_sz and cnt[nxt] < kk:
                    pos = nxt
                    kk -= cnt[nxt]
            return pos + 1

        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            upd(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                upd(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth((x + 1) // 2)
                med = vals[r - 1]
                c_le, s_le = pref(r)
                cost[i - x + 1] = (med * c_le - s_le) + ((total - s_le) - med * (x - c_le))

        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] != INF:
                    c = prev[i - x] + cost[i - x]
                    if c < cur[i]:
                        cur[i] = c
            prev = cur
        return prev[n]