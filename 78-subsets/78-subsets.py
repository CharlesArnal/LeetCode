class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        p_set = [{frozenset()}]
        for i in range(1,len(nums)+1):
            p_set.append({frozenset.union(frozenset({num}),subset) for num in nums for subset in p_set[-1]})
        return set().union(*p_set)
 
