class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        # for i in range(int((n+1)/2)):
        #     for j in range(int((n+1)/2)):
        #         print(matrix[i][j])
        #         print(matrix[n-1-j][i])
        #         print(matrix[n-1-i][n-1-j])
        #         print(matrix[j][n-1-i])
        #         print("---")
        #         matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] =  matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]

        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        for i in range(int((n+1)/2)):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        