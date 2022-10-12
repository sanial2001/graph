def solve(mat):
    grid = []
    for val in mat:
        grid.append(list(val))
    for val in grid:
        print(val)
    m, n = len(grid), len(grid[0])
    q = [(0, 0, 0)]
    visit = set()
    visit.add((0, 0, 0))
    steps = 1
    power = 0
    while q:
        num = len(q)
        for i in range(num):
            x, y, power = q.pop(0)
            if x == m - 1 and y == n - 1 and power <= 1:
                return steps
            if grid[x][y] == "+":
                if x > 0 and (x - 1, y, power) not in visit:
                    visit.add((x - 1, y, power))
                    q.append((x - 1, y, power))
                if y > 0 and (x, y - 1, power) not in visit:
                    visit.add((x, y - 1, power))
                    q.append((x, y - 1, power))
                if x < m - 1 and (x + 1, y, power) not in visit:
                    visit.add((x + 1, y, power))
                    q.append((x + 1, y, power))
                if y < n - 1 and (x, y + 1, power) not in visit:
                    visit.add((x, y + 1, power))
                    q.append((x, y + 1, power))
            elif grid[x][y] == "*":
                if x > 0 and y > 0 and (x - 1, y - 1, power) not in visit:
                    visit.add((x - 1, y - 1, power))
                    q.append((x - 1, y - 1, power))
                if x > 0 and y < n - 1 and (x - 1, y + 1, power) not in visit:
                    visit.add((x - 1, y + 1, power))
                    q.append((x - 1, y + 1, power))
                if x < m - 1 and y < n - 1 and (x + 1, y + 1, power) not in visit:
                    visit.add((x + 1, y + 1, power))
                    q.append((x + 1, y + 1, power))
                if x < m - 1 and y > 0 and (x + 1, y - 1, power) not in visit:
                    visit.add((x + 1, y - 1, power))
                    q.append((x + 1, y - 1, power))
            elif grid[x][y] == ".":
                power += 1
                if x > 0 and (x - 1, y, power) not in visit and power <= 1:
                    visit.add((x - 1, y, power))
                    q.append((x - 1, y, power))
                if y > 0 and (x, y - 1, power) not in visit and power <= 1:
                    visit.add((x, y - 1, power))
                    q.append((x, y - 1, power))
                if x < m - 1 and (x + 1, y, power) not in visit and power <= 1:
                    visit.add((x + 1, y, power))
                    q.append((x + 1, y, power))
                if y < n - 1 and (x, y + 1, power) not in visit and power <= 1:
                    visit.add((x, y + 1, power))
                    q.append((x, y + 1, power))
                if x > 0 and y > 0 and (x - 1, y - 1, power) not in visit and power <= 1:
                    visit.add((x - 1, y - 1, power))
                    q.append((x - 1, y - 1, power))
                if x > 0 and y < n - 1 and (x - 1, y + 1, power) not in visit and power <= 1:
                    visit.add((x - 1, y + 1, power))
                    q.append((x - 1, y + 1, power))
                if x < m - 1 and y < n - 1 and (x + 1, y + 1, power) not in visit and power <= 1:
                    visit.add((x + 1, y + 1, power))
                    q.append((x + 1, y + 1, power))
                if x < m - 1 and y > 0 and (x + 1, y - 1, power) not in visit and power <= 1:
                    visit.add((x + 1, y - 1, power))
                    q.append((x + 1, y - 1, power))
        steps += 1

    return -1


if __name__ == "__main__":
    print(solve(mat=["*++++", "+*.++", ".*.++", "*+++."]))



# 8 6
# 1 7 6
# 2 6 5
# 3 6 6
# 4 5 6
# 5 4 5
# 6 4 6
# 7 3 6
# 8 2 5
# 9 1 3
# 10 0 0

15 29

