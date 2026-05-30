class Solution:
    def pacificAtlantic(self, heights):
        
        rows, cols = len(heights), len(heights[0])
        
        pac = set()
        atl = set()
        
        def dfs(r, c, visit):
            
            visit.add((r, c))
            
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visit and
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, visit)
        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)
        
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        
        res = []
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res