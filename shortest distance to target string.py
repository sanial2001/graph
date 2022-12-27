class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        q = [[startIndex, words[startIndex]]]
        visit = set()
        visit.add(startIndex)
        steps = 0

        while q:
            num = len(q)
            for i in range(num):
                # print(q[0])
                index, word = q.pop(0)
                if word == target:
                    return steps
                if (index + 1) % n not in visit:
                    visit.add((index + 1) % n)
                    q.append(((index + 1) % n, words[(index + 1) % n]))
                if (index - 1 + n) % n not in visit:
                    visit.add((index - 1 + n) % n)
                    q.append(((index - 1 + n) % n, words[(index - 1 + n) % n]))
            if q: steps += 1

        return -1
