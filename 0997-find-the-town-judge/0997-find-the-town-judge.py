class Solution:
    def findJudge(self, n, trust):
        
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        for person in range(1, n + 1):
            
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person
        
        return -1