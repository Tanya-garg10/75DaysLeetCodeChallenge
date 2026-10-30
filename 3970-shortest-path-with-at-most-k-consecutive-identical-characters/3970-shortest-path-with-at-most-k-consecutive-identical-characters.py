import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1
        dist = {1: 0}          
        heap = [(0, 0, 1)]

        while heap:
            d, u, run = heapq.heappop(heap)
            if d > dist.get(u * K + run, float('inf')):
                continue
            if u == n - 1:
                return d
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    nr = run + 1
                    if nr > k:
                        continue
                else:
                    nr = 1
                nd = d + w
                key = v * K + nr
                if nd < dist.get(key, float('inf')):
                    dist[key] = nd
                    heapq.heappush(heap, (nd, v, nr))

        return -1