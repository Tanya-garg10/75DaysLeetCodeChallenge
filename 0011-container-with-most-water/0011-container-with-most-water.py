class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            
            max_area = max(max_area, area)
            
            # move the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area