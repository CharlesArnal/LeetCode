class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        solution = []
        for i in range(0,len(nums),2):
            solution.extend([nums[i+1]]*nums[i])
        return solution
            
        