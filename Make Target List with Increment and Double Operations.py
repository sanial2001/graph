class Solution:
    def solve(self, target):
        n = len(target)
        nums = [0] * n
        q = [nums]
        ans = 0
        visit = set()
        nums = [str(i) for i in nums]
        visit.add(''.join(nums))

        while q:
            num = len(q)
            for i in range(num):
                arr = q.pop(0)
                if arr == target:
                    return ans
                for j in range(len(arr)):
                    temp = arr[::]
                    temp[j] = arr[j] + 1
                    # print(temp)
                    x = [str(p) for p in temp]
                    visit_check = ''.join(x)
                    if visit_check not in visit:
                        visit.add(visit_check)
                        q.append(temp)
                temp = [val * 2 for val in arr]
                x = [str(p) for p in temp]
                visit_check = ''.join(x)
                if visit_check not in visit:
                    visit.add(visit_check)
                    q.append(temp)
            if q: ans += 1
