class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        if not dict:
            return 0
        
        max_length = 0
        s_lower = s.lower()
        set_lower = set()
        for word in dict:
            lower_word = word.lower()
            set_lower.add(lower_word)
            max_length = max(max_length, len(word))

        result = self.dfs(s_lower, 0, max_length, set_lower, {})
        return result

    def dfs(self, s_lower, index, max_length, set_lower, memo):
        if index in memo:
            return memo[index]
        if index == len(s_lower):
            return 1

        result = 0
        for end in range(index + 1, len(s_lower) + 1):
            if (end - index) > max_length:
                break

            word = s_lower[index:end]
            if word not in set_lower:
                continue
            result += self.dfs(s_lower, end, max_length, set_lower, memo)

        memo[index] = result
        return result