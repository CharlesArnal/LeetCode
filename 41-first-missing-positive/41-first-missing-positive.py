class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=0
        for i in range(n):
            if nums[i]!=0 :
                nums[nums[i]%(2*n) -1] += 2*n
        #print("array : ")
        #print(nums)
        for i in range(n):
            if nums[i]<=n+1:
                return i+1
        return n+1
 