class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        if nums[0] > 0:
            return []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0 and sorted([nums[i], nums[l], nums[r]]) not in res:
                    res.append(sorted([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1
                elif total < 0:
                    l +=1
                else:
                    r-=1
        return res
            