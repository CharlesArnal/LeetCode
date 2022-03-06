class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        sorted_list = sorted(enumerate(height),key=lambda x: x[1],reverse=True)
        print(sorted_list)
        left_b = len(height)+1
        greater_left = [False]*len(height)
        for i in range(len(height)):
            if sorted_list[i][0]>left_b:
                greater_left[i]=True
            else:
                left_b = sorted_list[i][0]
        right_b = -1
        greater_right = [False]*len(height)
        for i in range(len(height)):
            if sorted_list[i][0]<right_b:
                greater_right[i]=True
            else:
                right_b = sorted_list[i][0]
        bounds = sorted([x[0] for i,x in enumerate(sorted_list) if not (greater_left[i] and greater_right[i])])
        integral = 0
        for j in range(len(bounds)-1):
            min_max = min(height[bounds[j]],height[bounds[j+1]])
            integral += sum([min_max-x for x in height[bounds[j]+1:bounds[j+1]]])
        return integral
        """
        if len(height) in {1,2}:
            return 0
        max_1 = max(enumerate(height), key=lambda x: x[1])[0]
        #sorted_list = sorted(enumerate(height),key=lambda x: x[1],reverse=True)
        #max_1, max_2 = sorted_list[0][0], sorted_list[1][0]
        if max_1 not in {0,len(height)-1}:
            return self.trap(height[:max_1+1]) + self.trap(height[max_1:])
        max_2 = max(enumerate(height[1:]), key=lambda x: x[1])[0]+1 if max_1 == 0 else max(enumerate(height[:-1]), key=lambda x: x[1])[0]
        if max_2 not in {0,len(height)-1}:
            return self.trap(height[:max_2+1]) + self.trap(height[max_2:])
        min_max = min(height[0],height[-1])
        return sum([min_max-x for x in height[1:-1]])
        """
