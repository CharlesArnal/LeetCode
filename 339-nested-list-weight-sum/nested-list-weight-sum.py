# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def rec_comp(nesLis):
            raw_sum = 0
            weighted_sum = 0
            for el in nesLis:
                if el.isInteger():
                    raw_sum += el.getInteger()
                    weighted_sum += el.getInteger()
                else:
                    w_sum, r_sum = rec_comp(el.getList())
                    raw_sum += r_sum
                    weighted_sum += (w_sum + r_sum)
            return weighted_sum, raw_sum

        total_sum = 0
        for el in nestedList:
            if el.isInteger():
                total_sum += el.getInteger()
            else:
                w_sum, r_sum = rec_comp(el.getList())
                total_sum += (w_sum + r_sum)
        return total_sum

            
        