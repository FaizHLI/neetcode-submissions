class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search
        #we don't know num of rotations
        l,r = 0, len(nums)-1
        #we know at least one half of the array is sorted
        #we just have to find out which half
        while l<=r:
            m = (l +r) //2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: #first half is sorted 
                # check if target is in there
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m+1
                    # do binary search with these endpoints for the target
                #if not, search second half 
            else:
                #second half is sorted
                #check if target is in there
                if nums[m] <= target <=nums[r]:
                    l = m
                    #binary search on second half
                else:
                    r = m-1
                #if not, search first half

        return -1
                    