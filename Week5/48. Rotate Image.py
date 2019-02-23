class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size):
            for j in range(i + 1,size):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(size):
            matrix[i].reverse()
