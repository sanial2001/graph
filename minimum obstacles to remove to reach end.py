class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 0:
            q = [(0, 0, 0)]
        else:
            q = [(0, 0, 1)]
        visit = set()

        while q:
            cost, x, y = q.pop(0)
            # print(x, y, cost)
            if x == m - 1 and y == n - 1:
                return cost
            if x > 0 and (x - 1, y) not in visit:
                visit.add((x - 1, y))
                if grid[x - 1][y] == 0:
                    q.insert(0, (cost, x - 1, y))
                else:
                    q.append((cost + 1, x - 1, y))
            if y > 0 and (x, y - 1) not in visit:
                visit.add((x, y - 1))
                if grid[x][y - 1] == 0:
                    q.insert(0, (cost, x, y - 1))
                else:
                    q.append((cost + 1, x, y - 1))
            if x < m - 1 and (x + 1, y) not in visit:
                visit.add((x + 1, y))
                if grid[x + 1][y] == 0:
                    q.insert(0, (cost, x + 1, y))
                else:
                    q.append((cost + 1, x + 1, y))
            if y < n - 1 and (x, y + 1) not in visit:
                visit.add((x, y + 1))
                if grid[x][y + 1] == 0:
                    q.insert(0, (cost, x, y + 1))
                else:
                    q.append((cost + 1, x, y + 1))