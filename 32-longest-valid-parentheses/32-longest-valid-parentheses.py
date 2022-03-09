class Solution:
    def longestValidParentheses(self, s: str) -> int:
        my_stack = []
        max_l = 0
        max_indices = ()
        last_op_remove = False
        value_removed = None
        for i, car in enumerate(s):
            #print(f"my stack: {my_stack}")
            if car =="(":
                if last_op_remove:
                    my_stack.append(value_removed)
                else:
                    my_stack.append(i)
                last_op_remove = False
            if car ==")":
                if my_stack != []:
                    #print("test")
                    length = i-my_stack[-1]+1
                    if length> max_l:
                        max_l = length
                        max_indices = (my_stack[-1],i)
                    value_removed = my_stack[-1]
                    last_op_remove = True
                    my_stack.pop()
                    #print(max_indices)
                else:
                    last_op_remove = False
        return max_l 
                    
                    
        