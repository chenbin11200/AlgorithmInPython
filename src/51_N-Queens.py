import math

class NQueen(object):
    count = 0

    def NQueen(self, n):
        # type: (object, object) -> object
        #solution = [0 for i in range(8)]
        solution = [0] * 8
        self.PutQueenInLine(0, solution)

    def PrintSolution(self, solution):
        self.count += 1
        print 'Find a solution ' + str(self.count)
        print solution

    def PutQueenInLine(self, rowIndex, solution):
        # type: (rowIndex) -> int
        for columnIndex in range(8):
            if self.CanPutQueen(rowIndex, columnIndex, solution):
                solution[rowIndex] = columnIndex
                if rowIndex >= 7:
                    self.PrintSolution(solution)
                else:
                    self.PutQueenInLine(rowIndex + 1, solution)

    def CanPutQueen(self, rowIndex, columnIndex, solution):
        for row in range(rowIndex):
            if solution[row] == columnIndex or math.fabs(solution[row] - columnIndex) == math.fabs(row-rowIndex):
                return False
        return True


NQueen().NQueen(8)