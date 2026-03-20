class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        i = 0  # slow pointer
        
        for j in range(1, len(nums)):  # fast pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1