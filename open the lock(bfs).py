class Solution:
    def children(self, nums):
        nums = list(nums)
        ans = []
        for i in range(4):
            temp = nums[::]
            temp[i] = str((int(nums[i]) + 1) % 10)
            ans.append(''.join(temp))
            temp[i] = str((int(nums[i]) - 1) % 10)
            ans.append(''.join(temp))
        return ans

    def openLock(self, deadends, target: str) -> int:
        ans = 0
        q = ['0000']
        visit = set()
        visit.add('0000')
        while q:
            num = len(q)
            for i in range(num):
                parent = q.pop(0)
                # print(match)
                if parent == target:
                    return ans
                if parent in deadends:
                    continue
                for child in self.children(parent):
                    if child not in visit:
                        visit.add(child)
                        q.append(child)
            ans += 1
        return -1
