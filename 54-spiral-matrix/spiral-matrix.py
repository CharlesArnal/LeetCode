class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.partialSpiral(matrix, "h")        

    def partialSpiral(self, matrix: List[List[int]], direction)-> List[int]:
        if matrix == [] or matrix[0]==[]:
            return []
        match direction:
            case "h":
                return matrix[0] + self.partialSpiral(matrix[1:],"r")
            case "r":
                return [row[-1] for row in matrix] + self.partialSpiral([row[:-1] for row in matrix],"d")
            case "d":
                return list(reversed(matrix[-1])) + self.partialSpiral(matrix[:-1],"l")
            case "l":
                return [row[0] for row in reversed(matrix)] + self.partialSpiral([row[1:] for row in matrix],"h")
