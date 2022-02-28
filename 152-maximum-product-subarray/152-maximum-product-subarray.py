import numpy

def best_product(nums):
    size = len(nums)
    if size ==1:
        return nums[0]
    idx_list = [idx for idx, val in enumerate(nums) if val < 0]
    if len(idx_list)%2 ==0:
        return int(numpy.prod(nums))
    else:
        return int(max(numpy.prod(nums[0:idx_list[-1]]), numpy.prod(nums[idx_list[0]+1:])))
        
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        size = len(nums)
        idx_list = [idx + 1 for idx, val in enumerate(nums) if val == 0]
        split_list = [nums[i: j-1] for i, j in zip([0] + idx_list, idx_list + ([size+1] if (not idx_list or idx_list[-1] != size) else [])) if len(nums[i:j-1])!=0]
        if idx_list:
            current_max = max(current_max,0)
        if split_list:
            current_max = max(current_max,max([best_product(sublist) for sublist in split_list]))
        return current_max
  
