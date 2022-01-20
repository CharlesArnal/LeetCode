class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums=[]
        for num in nums:
            if num not in new_nums:
                new_nums += [num]*min(nums.count(num),3)
        #print(new_nums)
        nums = new_nums
        nums.sort()
        #print(nums)
        solution = []
        for i1, v1 in enumerate(nums):         
            lb=i1+1
            up=len(nums)-1
            #print("i1 = "+str(i1))
            while lb<up:
                if nums[lb]+nums[up] == -v1 and {v1,nums[lb],nums[up]} not in solution:
                        solution.append({v1,nums[lb],nums[up]})
                        #print("yay")
                elif nums[lb]+nums[up]> -v1:
                    #print("lb = "+str(lb))
                    while nums[lb]+nums[up]>-v1  and lb+1<up:
                        up-=1
                        #print("up = "+str(up))
                    if nums[lb]+nums[up] == -v1 and {v1,nums[lb],nums[up]} not in solution:
                        solution.append({v1,nums[lb],nums[up]})
                        #print("yay")
                    elif nums[lb]+nums[up]<-v1:
                        up+=1
                lb+=1
        return [[v for v in my_set] if len(my_set) ==3 else [v for v in my_set]+[-sum([v for v in my_set])] if len(my_set)==2 else [v for v in my_set]*3 for my_set in solution]
    