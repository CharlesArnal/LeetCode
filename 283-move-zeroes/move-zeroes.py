class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapping = []
        for i, elem in enumerate(nums):
            if elem!=0:
                mapping.append(i)
        for i in range(len(mapping)):
            nums[i] = nums[mapping[i]]
        for i in range(len(mapping),len(nums)):
            nums[i]=0


        