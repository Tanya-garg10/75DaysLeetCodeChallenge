from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        order = sorted(range(n), key=lambda i: intervals[i][0])
        starts = [intervals[order[i]][0] for i in range(n)]
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        def better(a, b):
            if a[0] != b[0]:
                return a[0] > b[0]
            return a[1] < b[1] 
        
        for i in range(n - 1, -1, -1):
            idx_i = order[i]
            l_i, r_i, w_i = intervals[idx_i]
            j = bisect_right(starts, r_i)  
            
            dp[i][0] = (0, [])
            for k in range(1, 5):
                skip = dp[i + 1][k]
                take_score = w_i + dp[j][k - 1][0]
                take_list = dp[j][k - 1][1] + [idx_i]
                take_list.sort()
                take = (take_score, take_list)
                
                dp[i][k] = take if better(take, skip) else skip
        
        return dp[0][4][1]