def solve(a, b):
    q = [a]
    visit = set()
    visit.add(a)
    steps = 0
    while q:
        num = len(q)
        for i in range(num):
            val = q.pop(0)
            if val == b:
                return steps
            if (val - 1) not in visit:
                visit.add(val - 1)
                q.append(val - 1)
            if (2 * val) not in visit:
                visit.add(2 * val)
                q.append(2 * val)
        if q: steps += 1
    return steps


if __name__ == "__main__":
    print(solve(6,21))
