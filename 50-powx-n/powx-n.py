from math import exp, log
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0 if n != 0 else 1
        if x<0:
            return exp(log(-x)*n) if n%2 == 0 else -exp(log(-x)*n)
        return exp(log(x)*n)
        