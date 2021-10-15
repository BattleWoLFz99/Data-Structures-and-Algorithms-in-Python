class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if words1 is None and words2 is None:
            return True
        if words1 is None or words2 is None:
            return False
        if len(words1) != len(words2):
            return False

        d = dict()
        for pair in pairs:
            word1 = pair[0]
            word2 = pair[1]
            d[word1] = d.get(word1, set())
            d[word1].add(word2)
            d[word2] = d.get(word2, set())
            d[word2].add(word1)

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words2[i] not in d[words1[i]]:
                return False

        return True

        