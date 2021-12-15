class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        if not S:
            return [""]

        results = []
        self.dfs(S, 0, [], results)

        return results

    def dfs(self, S, index, current, results):
        if index == len(S):
            results.append("".join(current))
            return

        for c in self.get_next_char(S[index]):
            current.append(c)
            self.dfs(S, index + 1, current, results)
            current.pop()

    def get_next_char(self, char):
        if char.islower():
            return [char, char.upper()]
        if char.isupper():
            return [char, char.lower()]
        return [char]