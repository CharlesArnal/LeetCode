class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i == 0:
            nums.reverse()
        else:
            i-=1
            temp=nums[i]
            j=i
            while j+1<len(nums) and nums[j+1]>temp :
                j+=1
            nums[i]=nums[j]
            nums[j]=temp
            for k in range(floor((len(nums)-(i+1))/2)):
                temp2 = nums[i+1+k]
                nums[i+1+k] = nums[len(nums)-1-k]
                nums[len(nums)-1-k] = temp2

        """
        Do not return anything, modify nums in-place instead.
        """
        

