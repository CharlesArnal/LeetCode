

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>= target:
            return 0
        nums = nums + [nums[-1]+1+abs(target)]*(2**(floor(log(len(nums))/log(2))+1)-len(nums))
        lower_bound = 0
        L = len(nums)
        k=1
        while nums[lower_bound+1]<target:
            if nums[lower_bound + int(L/2**k)]<target:
                lower_bound = lower_bound + int(L/2**k)
            k = k+1 
        return lower_bound +1
            
