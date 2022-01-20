class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_possible = len(nums)-1
        last_tested = len(nums)-1
        while last_tested>0:
            last_tested-=1
            if nums[last_tested]>=last_possible-last_tested :
                last_possible = last_tested
        if last_possible==0:
            return True
        else:
            return False
        
    