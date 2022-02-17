from scipy.signal import convolve2d
import numpy

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(entry) for entry in line] for line in matrix]
        N = min(len(matrix),len(matrix[0]))
        my_max = numpy.amax(matrix)
        if N == 1 or my_max == 0:
            return my_max
        k=1
        while(k<N):
            matrix = convolve2d(matrix, numpy.ones((2,2)), mode='valid')
            if numpy.amax(matrix) == 4**k:
                k+=1
            else:
                return k**2
        return k**2
