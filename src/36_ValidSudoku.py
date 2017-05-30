import collections

class Solution(object):
    def isValidSudoku(self, board):
        test = [x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i / 3, j / 3, c))]

        print collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i / 3, j / 3, c))
        ).values()


        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i / 3, j / 3, c))
        ).values() + [1])

print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])