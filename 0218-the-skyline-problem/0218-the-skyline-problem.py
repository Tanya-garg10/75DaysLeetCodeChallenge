import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))  
            events.append((r, 0, 0))  

        events.sort()

        res = []
        heap = [(0, float('inf'))] 

        for x, negh, r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if negh:
                heapq.heappush(heap, (negh, r))
            while heap[0][1] <= x:
                heapq.heappop(heap)
            cur = -heap[0][0]
            if not res or res[-1][1] != cur:
                res.append([x, cur])

        return res