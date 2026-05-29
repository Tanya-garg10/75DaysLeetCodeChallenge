class Solution:
    def cloneGraph(self, node):
        
        if not node:
            return None
        
        oldToNew = {}
        
        def dfs(node):
            
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)