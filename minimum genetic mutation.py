class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        visit = set()
        visit.add(start)
        q = [start]
        steps = 0
        bank.append(start)
        choice = ['A', 'C', 'G', 'T']

        while q:
            num = len(q)
            for _ in range(num):
                match = q.pop(0)
                if match == end:
                    return steps
                if match not in bank:
                    continue
                for i in range(8):
                    for j in range(4):
                        temp = match[:i] + choice[j] + match[i + 1:]
                        if temp not in visit:
                            visit.add(temp)
                            q.append(temp)
            if q: steps += 1

        return -1
