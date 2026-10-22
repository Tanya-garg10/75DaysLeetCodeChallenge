from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        start = None
        if all((nums[i] - i) % n == nums[0] for i in range(n)):
            start = (0, nums[0] % n)
        elif all((nums[i] + i) % n == nums[0] for i in range(n)):
            start = (1, nums[0] % n)
        else:
            return -1

        if start == (0, 0):
            return 0

        dist = [-1] * (2 * n)
        s = start[0] * n + start[1]
        dist[s] = 0
        q = deque([s])
        target = 0  

        while q:
            cur = q.popleft()
            t, p = divmod(cur, n)
            if t == 0:
                nxt = [(0, (p + 1) % n), (1, (p - 1) % n)]
            else:
                nxt = [(1, (p - 1) % n), (0, (p + 1) % n)]
            for nt, np_ in nxt:
                idx = nt * n + np_
                if dist[idx] == -1:
                    dist[idx] = dist[cur] + 1
                    if idx == target:
                        return dist[idx]
                    q.append(idx)

        return -1