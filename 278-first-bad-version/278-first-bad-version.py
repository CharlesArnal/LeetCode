# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n
        while lower_bound<upper_bound :
            mid = lower_bound + floor((upper_bound-lower_bound)/2)
            if isBadVersion(mid):
                upper_bound = mid
            else :
                lower_bound = mid + 1
        return lower_bound  
 