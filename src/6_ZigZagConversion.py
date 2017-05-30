class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        evenColumnIndex = True
        result = []
        stringLength = len(s)

        if numRows >= stringLength or numRows == 1:
            return s

        fullLine = numRows
        groupLine = 2 * fullLine - 2
        i = rowIndex = 0

        for rowIndex in range(0, fullLine):
            i = rowIndex
            evenColumnIndex = True
            while i < stringLength:
                result.append(s[i])
                if rowIndex == 0 or rowIndex == numRows - 1:
                    i = i + groupLine
                else:
                    if evenColumnIndex:
                        i = i + groupLine - rowIndex * 2
                    else:
                        i = i + rowIndex * 2
                evenColumnIndex = not evenColumnIndex
            rowIndex = rowIndex + 1
        return ''.join(result)

class BestSolution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)


# This is NOT zigzag conversion, instead it is
# 1   5   9
# 2 4 6 8 .
# 3   7   .
class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        evenRowIndex = evenColumnIndex = True
        result = []
        stringLength = len(s)

        if numRows >= stringLength or numRows == 1:
            return s

        fullLine = numRows
        leckLine = (numRows + 1) / 2
        groupLine = 2 * fullLine - leckLine
        i = rowIndex = 0

        for rowIndex in range(0, fullLine):
            i = rowIndex
            evenColumnIndex = True
            while i < stringLength:
                if evenRowIndex:
                    result.append(s[i])
                    i = i + groupLine

                else:
                    result.append(s[i])
                    if evenColumnIndex:
                        i = i + (fullLine - rowIndex - 1) + (rowIndex + 1) / 2
                    else:
                        i = i + (fullLine - leckLine) - rowIndex / 2 + rowIndex
                evenColumnIndex = not evenColumnIndex
            rowIndex = rowIndex + 1
            evenRowIndex = not evenRowIndex

        return ''.join(result)

print BestSolution().convert('abc', 2)