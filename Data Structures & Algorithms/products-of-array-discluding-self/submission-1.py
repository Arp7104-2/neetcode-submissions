class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefixProd = [1]
        for i in range(1, len(nums)):
            prefixProd.append(nums[i - 1] * prefixProd[i - 1])
            
        suffixProd = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            res.append(prefixProd[i] * suffixProd[i])

        return res