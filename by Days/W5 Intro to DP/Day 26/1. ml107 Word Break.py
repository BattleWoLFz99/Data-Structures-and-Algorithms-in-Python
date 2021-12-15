# StackOverflow memo search ver.

class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return True
        if not wordSet:
            return False

        max_length = 0
        for word in wordSet:
            max_length = max(max_length, len(word))

        return self.dfs(s, 0, max_length, wordSet, {})

    def dfs(self, s, index, max_length, wordSet, memo):
        if index in memo:
            return memo[index]
            
        if index == len(s):
            return True

        for end in range(index + 1, len(s) + 1):
            if (end - index) > max_length:
                break

            word = s[index:end]

            if word not in wordSet:
                continue

            if self.dfs(s, end, max_length, wordSet, memo):
                return True

        memo[index] = False

        return False

s = Solution()
wordSet = set(["h", "e", "hel", "he", "lo", "world", "hell"])
print(s.wordBreak("helloworld", wordSet))