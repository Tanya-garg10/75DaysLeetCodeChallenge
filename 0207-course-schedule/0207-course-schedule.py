from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        completed = 0
        
        while q:
            node = q.popleft()
            completed += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    q.append(nei)
        
        return completed == numCourses