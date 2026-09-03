class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(x % 2 == 0 for x in nums1):
            return True

        return min(nums1) % 2 == 1