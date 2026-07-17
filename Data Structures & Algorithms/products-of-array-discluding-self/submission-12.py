class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix 
        prefix = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]
        postfix = [1] * len(nums)
        prod = 1
        for j in range(len(nums)-1, -1 ,-1):
            postfix[j] = prod
            prod *= nums[j]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res
        # for j in range(len(nums)-1, -1, -1):
            