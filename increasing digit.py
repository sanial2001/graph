class Solution:
    def solve(self, n):
        q = [i + 1 for i in range(9)]
        ans = 0
        while q:
            val = str(q.pop(0))
            if len(val) == n:
                # print(val)
                ans += 1
            last = val[-1]
            for i in range(int(last) + 1, 10):
                new_val = val + str(i)
                if len(str(new_val)) <= n:
                    q.append(int(new_val))
        return ans
