from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        counts = defaultdict(int)
        active = 0                 
        res = [0] * len(queries)

        right = 0  
        left = 0   

        for qi in order:
            q = queries[qi]
            lo, hi = q - x, q

            while right < len(logs) and logs[right][1] <= hi:
                sid = logs[right][0]
                if counts[sid] == 0:
                    active += 1
                counts[sid] += 1
                right += 1

            while left < right and logs[left][1] < lo:
                sid = logs[left][0]
                counts[sid] -= 1
                if counts[sid] == 0:
                    active -= 1
                left += 1

            res[qi] = n - active

        return res