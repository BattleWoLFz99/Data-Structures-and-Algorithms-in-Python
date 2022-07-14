# end BFS 找可行拿去 DFS 剪枝
# LeetCode 的写法，记得加 beginWord。。
# 是到现在符合个人模板的写法，多了个 next_words_options 然后用 +1 判断多解
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList:
            return []
        if beginWord == endWord:
            return []
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        word_set.add(beginWord)
        distance, next_words_options = self.bfs(beginWord, endWord, word_set)
        results = []
        self.dfs(beginWord, endWord, next_words_options, distance, [beginWord], results)
        
        return results
        
    def bfs(self, beginWord, endWord, word_set):
        from collections import defaultdict
        distance = {}
        distance[endWord] = 0
        next_words_options = defaultdict(set)
        queue = collections.deque([endWord])
        while queue:
            word = queue.popleft()
            if word == beginWord:
                break
            for next_word in self.get_next_words(word, word_set):
                if next_word not in distance:
                    next_words_options[next_word].add(word)
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
                elif distance[next_word] == distance[word] + 1:
                    next_words_options[next_word].add(word)
                    
        return distance, next_words_options
    
    def get_next_words(self, word, word_set):
        next_words = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == word[i]:
                    continue
                begin, end = word[:i], word[i + 1:]
                next_word = begin + c + end
                if next_word in word_set:
                    next_words.append(next_word)
                    
        return next_words
    
    def dfs(self, curr_word, endWord, next_words_options, distance, path, results):
        if curr_word == endWord:
            results.append(list(path))
            
        for next_word in next_words_options[curr_word]:
            if distance[next_word] != distance[curr_word] - 1:
                continue
            path.append(next_word)
            self.dfs(next_word, endWord, next_words_options, distance, path, results)
            path.pop()