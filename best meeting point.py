class Solution:
    def solve(self, matrix):
        m, n = len(matrix), len(matrix[0])
        ans = [[float("inf") for _ in range(n)] for _ in range(m)]
        q = []
        visit = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 2:
                    q.append((i, j, i, j, 0))
                    visit.add((i, j, i, j))

        while q:
            num = len(q)
            for i in range(num):
                ox, oy, x, y, moves = q.pop(0)
                if ans[x][y] == float("inf"):
                    ans[x][y] = moves
                else:
                    ans[x][y] += moves

                if x > 0 and matrix[x - 1][y] != 1 and (ox, oy, x - 1, y) not in visit:
                    q.append((ox, oy, x - 1, y, moves + 1))
                    visit.add((ox, oy, x - 1, y))
                if y > 0 and matrix[x][y - 1] != 1 and (ox, oy, x, y - 1) not in visit:
                    q.append((ox, oy, x, y - 1, moves + 1))
                    visit.add((ox, oy, x, y - 1))
                if x < m - 1 and matrix[x + 1][y] != 1 and (ox, oy, x + 1, y) not in visit:
                    q.append((ox, oy, x + 1, y, moves + 1))
                    visit.add((ox, oy, x + 1, y))
                if y < n - 1 and matrix[x][y + 1] != 1 and (ox, oy, x, y + 1) not in visit:
                    q.append((ox, oy, x, y + 1, moves + 1))
                    visit.add((ox, oy, x, y + 1))

        res = float("inf")
        for val in ans:
            res = min(res, min(val))

        return res
