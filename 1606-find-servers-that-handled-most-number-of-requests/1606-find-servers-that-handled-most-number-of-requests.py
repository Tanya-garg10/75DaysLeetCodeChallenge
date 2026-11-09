import heapq
from bisect import bisect_left, insort

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))
        busy = []
        cnt = [0] * k

        for i, t in enumerate(arrival):
            while busy and busy[0][0] <= t:
                _, s = heapq.heappop(busy)
                insort(free, s)
            if not free:
                continue
            pos = bisect_left(free, i % k)
            if pos == len(free):
                pos = 0
            s = free.pop(pos)
            cnt[s] += 1
            heapq.heappush(busy, (t + load[i], s))

        mx = max(cnt)
        return [s for s in range(k) if cnt[s] == mx]