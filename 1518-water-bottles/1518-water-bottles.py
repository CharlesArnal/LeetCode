class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        solution = numBottles
        while numBottles>=numExchange:
            solution = solution + floor(numBottles/numExchange)
            numBottles = floor(numBottles/numExchange)+numBottles%numExchange
        return solution
            
        