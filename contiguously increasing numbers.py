class Solution:
    def solve(self, start, end):
        q = [i + 1 for i in range(9)]
        ans = []
        while q:
            val = q.pop()
            if start <= val <= end:
                ans.append(val)
            last = str(val)[-1]
            if int(last) < 9:
                new = str(val) + str(int(last) + 1)
                if int(new) <= end: q.append(int(new))
        return sorted(ans)
