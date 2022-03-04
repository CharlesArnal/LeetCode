class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row<len(matrix)-1 and matrix[row+1][0]<=target :
            row+=1
        return (target in matrix[row])