import collections


class Solution:
    def depth(self, graph, start, end):
        visit = set()
        visit.add(start)
        ans = 1
        q = [start]
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == end:
                    return ans
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            ans += 1
        return 0

    def dfs(self, graph, word, k, depth, path, ans, visit, end):
        if k >= depth:
            if k == depth and word == end:
                ans.append(path[::])
            return
        # print(path)
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            for nei in graph[pattern]:
                if nei not in visit:
                    visit.add(nei)
                    path.append(nei)
                    self.dfs(graph, nei, k + 1, depth, path, ans, visit, end)
                    path.pop()
                    visit.remove(nei)

    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return []
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        depth = self.depth(graph, beginWord, endWord)
        if depth == 0:
            return []
        path, ans = [beginWord], []
        visit = set()
        visit.add(beginWord)
        self.dfs(graph, beginWord, 1, depth, path, ans, visit, endWord)
        # print(ans)
        return ans