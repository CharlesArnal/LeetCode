from numpy import argsort
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        # list of (value, position)
        my_stack = []#[heights[0],0]
        current_max = heights[0]
        for index, value in enumerate(heights):
            while len(my_stack) !=0 and my_stack[-1][0]>=value:
                if len(my_stack)>=2:
                    current_max = max(current_max,my_stack[-1][0]*(index-my_stack[-2][1]-1))
                else:
                    current_max = max(current_max,my_stack[-1][0]*index)
                current_max = max(current_max, my_stack[-1][0]*(index-my_stack[-1][1]))
                my_stack.pop()
            my_stack.append((value, index))
        while len(my_stack)!= 0:
            if len(my_stack)>=2:
                current_max = max(current_max,my_stack[-1][0]*(n-my_stack[-2][1]-1))
            else:
                current_max = max(current_max,my_stack[-1][0]*n)
            my_stack.pop()
            
        
        return current_max