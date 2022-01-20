class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_max = 0
        lb=0
        up=len(height)-1
        current_max = max(current_max,(up-lb)*min(height[up],height[lb]))
        while lb<up: # and min(lb,up)<max(height[lb:up]):
            if height[lb]<height[up]:
                lb+=1
            else:
                up-=1
            current_max = max(current_max,(up-lb)*min(height[up],height[lb]))
        return current_max
