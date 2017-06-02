# In order to test whether it will be faster to avoid creating whirling matrix
# Seems the performance is similar. This dumb version is a little bit faster, but too much code and hard to maintain.
class Solution(object):
    def __init__(self):
        self.counterRow = 1
        self.counterColumn = 1
        self.upBorder = 0
        self.downBorder = 0
        self.leftBorder = 0
        self.rightBorder = 0
        self.result = []
        self.sumLengh = 0

    def spiralOrder(self, matrix):
        '''
        :type matrix: List[List[int]]
        :rtype: List[int]
        '''

        if not matrix:
            return self.result

        m = len(matrix)
        n = len(matrix[0])

        self.downBorder = m
        self.rightBorder = n

        while self.sumLengh < m * n:
            if self.counterRow % 2 == 1:
                self.readRow(matrix, self.upBorder)
            else:
                self.readRow(matrix, self.downBorder-1)
            if self.sumLengh <= m * n:
                if self.counterColumn % 2 == 1:
                    self.readColumn(matrix, self.rightBorder-1)
                else:
                    self.readColumn(matrix, self.leftBorder)

        return self.result

    def readRow(self, matrix, rowIndex):
        for column in range(self.leftBorder, self.rightBorder)[:: 1 if self.counterRow % 2 == 1 else -1]:
            self.result.append(matrix[rowIndex][column])
            self.sumLengh += 1

        if self.counterRow % 2 == 0:
            self.downBorder -= 1
        else:
            self.upBorder += 1
        self.counterRow += 1

    def readColumn(self, matrix, columnIndex):
        for row in range(self.upBorder, self.downBorder)[:: 1 if self.counterColumn % 2 == 1 else -1]:
            self.result.append(matrix[row][columnIndex])
            self.sumLengh += 1

        if self.counterColumn % 2 == 1:
            self.rightBorder -= 1
        else:
            self.leftBorder += 1
        self.counterColumn += 1


print Solution().spiralOrder([
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
])

print Solution().spiralOrder([])
