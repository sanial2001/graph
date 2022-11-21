class Solution:
    def move(self, matrix, row, col):
        i, j = row - 1, col
        while i >= 0:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                i -= 1

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                i, j = i - 1, j - 1

        i, j = row, col - 1
        while j >= 0:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                j -= 1

        i, j = row + 1, col - 1
        while i < 8 and j >= 0:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                i, j = i + 1, j - 1

        i, j = row + 1, col
        while i < 8:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                i += 1

        i, j = row + 1, col + 1
        while i < 8 and j < 8:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                i, j = i + 1, j + 1

        i, j = row, col + 1
        while j < 8:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                j += 1

        i, j = row - 1, col + 1
        while i >= 0 and j < 8:
            if matrix[i][j] == 'Q':
                break
            elif matrix[i][j] == 'K':
                return True
            else:
                i, j = i - 1, j + 1

        return False

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        matrix = [['0' for _ in range(8)] for _ in range(8)]
        for i, j in queens:
            matrix[i][j] = 'Q'
        matrix[king[0]][king[1]] = 'K'
        '''
        for val in matrix:
            print(val)
        '''
        for i, j in queens:
            if self.move(matrix, i, j):
                res.append([i, j])

        return res
