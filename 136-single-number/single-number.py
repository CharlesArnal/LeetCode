class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dic = {}
        for entry in nums:
            if entry in my_dic:
                my_dic.pop(entry)
            else:
                my_dic[entry]=1
        return list(my_dic.keys())[0]
        