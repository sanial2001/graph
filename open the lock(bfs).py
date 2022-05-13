class Solution:
    def __init__(self):
        self.d = {
            '0': ['9', '1'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0'],
        }

    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set()
        visit.add('0000')
        q = ['0000']
        steps = 0

        while q:
            num = len(q)
            for i in range(num):
                match = q.pop(0)
                if match == target:
                    return steps
                if match in deadends:
                    continue
                for i in range(4):
                    key = match[i]
                    for j in range(2):
                        temp = match[:i] + self.d[key][j] + match[i + 1:]
                        # print(match, temp)
                        if temp not in visit:
                            visit.add(temp)
                            q.append(temp)
            if q: steps += 1
        return -1


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
