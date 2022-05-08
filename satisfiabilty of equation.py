class Solution:
    def find(self, x):
        if x not in self.parent:
            return x
        else:
            return self.find(self.parent[x])

    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = {}
        for equation in equations:
            if equation[1] == '=':
                x = self.find(equation[0])
                y = self.find(equation[-1])
                if x != y:
                    self.parent[y] = x

        for equation in equations:
            if equation[1] == '!':
                if self.find(equation[0]) == self.find(equation[-1]):
                    return False
        return True
