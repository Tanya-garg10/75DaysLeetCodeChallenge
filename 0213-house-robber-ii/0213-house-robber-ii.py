class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp

            return prev1

        return max(
            rob_linear(nums[:-1]),  
            rob_linear(nums[1:])    
        )