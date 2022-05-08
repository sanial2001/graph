import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        # print(graph.items())

        q = [beginWord]
        ans = 1
        visit = set()
        visit.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return ans
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            ans += 1
        return 0