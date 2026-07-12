class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
       
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, component)

        ans = 0

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                vertices = len(component)
                edge_count = 0

                for node in component:
                    edge_count += len(adj[node])

                edge_count //= 2  

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans