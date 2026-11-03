class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for x in nums:
            xor_all ^= x

        low_bit = xor_all & -xor_all

        a = 0
        for x in nums:
            if x & low_bit:
                a ^= x

        return [a, xor_all ^ a]