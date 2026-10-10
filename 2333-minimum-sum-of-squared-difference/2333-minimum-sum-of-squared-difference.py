class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        n = len(nums1)
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        mx = max(d)
        if sum(d) <= k:
            return 0

        cnt = [0] * (mx + 2)
        for x in d:
            cnt[x] += 1

        total = 0 
        v = mx
        while v > 0:
            total += cnt[v]
            if total > 0:
                if k >= total:
                    k -= total       
                else:
                    break            
            v -= 1
        else:
            return 0                 

        res = (total - k) * v * v + k * (v - 1) * (v - 1)
        for u in range(v):
            res += cnt[u] * u * u
        return res