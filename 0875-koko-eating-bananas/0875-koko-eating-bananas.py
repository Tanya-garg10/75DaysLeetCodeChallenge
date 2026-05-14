class Solution:
    def minEatingSpeed(self, piles, h):
        
        def canFinish(speed):
            hours = 0
            
            for pile in piles:
                hours += (pile + speed - 1) // speed
            
            return hours <= h
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left