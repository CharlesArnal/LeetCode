class Solution:
    def numSquares(self, n: int) -> int:
        solutions =[0,1]
        while len(solutions)<n+1:
            #print(str(floor(math.sqrt(len(solutions)+1))+1))
            #print([-i**2 for i in range(1,floor(math.sqrt(len(solutions)))+1)] )
            solutions.append(min(  [1+solutions[-i**2] for i in range(1,floor(math.sqrt(len(solutions)))+1)]    ))
        return solutions[-1]
        