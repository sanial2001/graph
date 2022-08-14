class Solution:
    def solve(self, nums):
        n = len(nums)
        d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        q = [(nums[0], 0)]
        visit = set()
        visit.add(0)
        steps = 0
        while q:
            num = len(q)
            for i in range(num):
                val, index = q.pop(0)
                # print(val, index, steps)
                if index == n - 1:
                    return steps
                if val in d:
                    for idx in d[val]:
                        if idx not in visit:
                            q.append((val, idx))
                            visit.add(idx)
                    del d[val]
                if (index + 1) < n and (index + 1) not in visit:
                    q.append((nums[index + 1], index + 1))
                    visit.add(index + 1)
                if (index - 1) > 0 and (index - 1) not in visit:
                    q.append((nums[index - 1], index - 1))
                    visit.add(index - 1)

            if q: steps += 1
