class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if not strs:
            return 0

        words_set = set(strs)
        visited = set()
        count = 0
        for word in strs:
            if word in visited:
                continue
            count += 1
            self.bfs(word, words_set, visited)

        return count

    def bfs(self, word, words_set, visited):
        queue = collections.deque([word])
        visited.add(word)
        while queue:
            curr_word = queue.popleft()
            for neighbor_word in self.get_neighbor_words(curr_word, words_set):
                if neighbor_word in visited:
                    continue
                queue.append(neighbor_word)
                visited.add(neighbor_word)
    
    def get_neighbor_words(self, curr_word, words_set):
        if len(curr_word) ** 2 < len(words_set):
            return self.get_neighbor_words_v1(curr_word, words_set)
        return self.get_neighbor_words_v2(curr_word, words_set)
        
    def get_neighbor_words_v1(self, curr_word, words_set):
        n = len(curr_word)
        curr_word_list = list(curr_word)
        neighbor_words = []
        for i in range(n):
            for j in range(i + 1, n):
                curr_word_list[i], curr_word_list[j] = \
                    curr_word_list[j], curr_word_list[i]
                converted_word = ''.join(curr_word_list)
                if converted_word in words_set:
                    neighbor_words.append(converted_word)
                curr_word_list[i], curr_word_list[j] = \
                curr_word_list[j], curr_word_list[i]
                    
        return neighbor_words
    
    def get_neighbor_words_v2(self, curr_word, words_set):
        neighbor_words = []
        for neighbor in words_set:
            if self.is_similar(curr_word, neighbor):
                neighbor_words.append(neighbor)
        
        return neighbor_words
    
    def is_similar(self, word1, word2):
        diff = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1
        return diff == 2