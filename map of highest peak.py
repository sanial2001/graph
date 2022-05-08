class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        visited = set()
        q = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    visited.add((i, j))
                    q.append((i, j))
                    isWater[i][j] = 0

        while q:
            num = len(q)
            for i in range(num):
                x, y = q.pop(0)
                val = isWater[x][y]
                if x > 0 and (x - 1, y) not in visited:
                    isWater[x - 1][y] = val + 1
                    visited.add((x - 1, y))
                    q.append((x - 1, y))
                if y > 0 and (x, y - 1) not in visited:
                    isWater[x][y - 1] = val + 1
                    visited.add((x, y - 1))
                    q.append((x, y - 1))
                if x < m - 1 and (x + 1, y) not in visited:
                    isWater[x + 1][y] = val + 1
                    visited.add((x + 1, y))
                    q.append((x + 1, y))
                if y < n - 1 and (x, y + 1) not in visited:
                    isWater[x][y + 1] = val + 1
                    visited.add((x, y + 1))
                    q.append((x, y + 1))

        return isWater
