class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # prefix
        pref = 1
        for i in range(n):
            ans[i] = pref
            pref *= nums[i]
        
        # suffix
        suff = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]
        
        return ans