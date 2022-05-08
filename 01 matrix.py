class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])

        int_max = 100000
        ans = int_max
        while q:
            num = len(q)
            for i in range(num):
                x, y = q.pop(0)
                if x > 0 and mat[x - 1][y] == 1:
                    mat[x - 1][y] = ans + 1
                    q.append([x - 1, y])
                if y > 0 and mat[x][y - 1] == 1:
                    mat[x][y - 1] = ans + 1
                    q.append([x, y - 1])
                if x < m - 1 and mat[x + 1][y] == 1:
                    mat[x + 1][y] = ans + 1
                    q.append([x + 1, y])
                if y < n - 1 and mat[x][y + 1] == 1:
                    mat[x][y + 1] = ans + 1
                    q.append([x, y + 1])
            if q: ans += 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = mat[i][j] - int_max

        return mat
