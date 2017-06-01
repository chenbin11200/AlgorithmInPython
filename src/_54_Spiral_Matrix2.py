class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            result = result + matrix[0]
            del matrix[0]
            matrix = map(list, zip(*matrix))[::-1]
        return result

print Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])

print Solution().spiralOrder(None)
