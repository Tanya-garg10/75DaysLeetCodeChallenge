class Solution:
    def minCostClimbingStairs(self, cost):
        
        a = cost[0]
        b = cost[1]
        
        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)
        
        return min(a, b)