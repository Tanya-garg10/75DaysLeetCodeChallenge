from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()     
        S = 0           
        tot = 0  
        r = n - 1
        ans = 0
        for l in range(n - 1, -1, -1):
            tot += nums[l]
            while dq and nums[dq[0]] <= nums[l]:
                f = dq.popleft()
                nxt = dq[0] if dq else r + 1
                S -= nums[f] * (nxt - f)
            end = dq[0] if dq else r + 1
            S += nums[l] * (end - l)
            dq.appendleft(l)
            while S - tot > k:
                S -= nums[dq[-1]]
                tot -= nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans