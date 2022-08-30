class Solution:
    def solve(self, cows):
        cows = list(cows)
        n = len(cows)
        q = []
        time = [0] * n

        for i, cow in enumerate(cows):
            if cow == "L":
                q.append(("L", i))
            if cow == "R":
                q.append(("R", i))

        while q:
            pos, i = q.pop(0)
            # print(cows)
            if i > 0 and pos == "L":
                if time[i - 1] == time[i] + 1:
                    cows[i - 1] = "@"
                    pass
                elif cows[i - 1] == "@":
                    cows[i - 1] = "L"
                    time[i - 1] = time[i] + 1
                    q.append(("L", i - 1))
            if i < n - 1 and pos == "R":
                if time[i + 1] == time[i] + 1:
                    cows[i - 1] = "@"
                    pass
                elif cows[i + 1] == "@":
                    cows[i + 1] = "R"
                    time[i + 1] = time[i] + 1
                    q.append(("R", i + 1))

        return ''.join(cows)
