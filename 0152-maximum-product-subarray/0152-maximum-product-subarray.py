class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            candidates = (num, max_ending_here * num, min_ending_here * num)
            max_ending_here = max(candidates)
            min_ending_here = min(candidates)
            
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far