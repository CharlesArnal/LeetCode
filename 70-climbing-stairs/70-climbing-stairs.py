from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        k=2
        a=1
        b=2
        while k<n:
            b,a = a+b,b
            k+=1
        return b
        