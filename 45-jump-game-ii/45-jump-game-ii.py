import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [0]
        for i in range(2,len(nums)+1):
            min_jumps.insert(0,(math.inf  if nums[-i]==0 else min([1+min_jumps[j] for j in range(min(nums[-i],len(min_jumps)))]) ) )
        return min_jumps[0]