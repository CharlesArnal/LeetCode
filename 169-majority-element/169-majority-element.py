class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for x in nums:
            if x not in my_dict:
                my_dict[x] = 1
            else:
                my_dict[x]+=1
        current_max = 0
        solution = 0
        #print(my_dict)
        for x in my_dict:
            #print(x)
            if my_dict[x]>current_max:
                current_max = my_dict[x]
                solution = x
                
        return solution