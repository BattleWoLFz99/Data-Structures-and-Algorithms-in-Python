class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        if not wordDict:
            []

        max_length = 0
        for word in wordDict:
            max_length = max(max_length, len(word))
        
        memo = {}
        results = []
        self.dfs(s, 0, max_length, wordDict, [], results, memo)

        return results

    def dfs(self, s, index, max_length, wordDict, path, results, memo):
        if index == len(s):
            results.append(" ".join(path))
            return

        if not self.is_possible(s, index, max_length, wordDict, memo):
            return

        for end in range(index + 1, len(s) + 1):
            if (end - index) > max_length:
                break
            word = s[index:end]
            if word not in wordDict:
                continue
            
            path.append(word)
            self.dfs(s, end, max_length, wordDict, path, results, memo)
            path.pop()

    def is_possible(self, s, index, max_length, wordDict, memo):
        if index in memo:
            return memo[index]

        if index == len(s):
            return True

        for end in range(index + 1, len(s) + 1):
            if (end - index) > max_length:
                break

            word = s[index:end]
            if word not in wordDict:
                continue
            if self.is_possible(s, end, max_length, wordDict, memo):
                return True

        memo[index] = False
        return False