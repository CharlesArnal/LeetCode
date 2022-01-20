class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_suba = [nums[0]]
        sum_suba_up =[nums[0]]
        for i in range(1,len(nums)):
            sum_suba.append(max(sum_suba[-1], sum_suba_up[-1]+nums[i], nums[i]))
            sum_suba_up.append(max(sum_suba_up[-1] + nums[i], nums[i])  )
        return sum_suba[-1]