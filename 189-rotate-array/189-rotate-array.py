import numpy as np

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        """
        L = len(nums)
        gcd = np.gcd(L,k)
        x = int(L/gcd)
        for bc in range(gcd):
            temp = nums[bc]
            for i in range(0,x-1):
                nums[(bc-i*k)%L] = nums[(bc-(i+1)*k)%L]
            nums[(bc-(x-1)*k)%L] = temp
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        