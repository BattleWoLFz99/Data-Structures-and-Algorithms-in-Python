# LeetCode Ver.
# wordList is actually a list holy shit....
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if not wordList:
            return 0
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        forward_queue = collections.deque([beginWord])
        forward_set = set([beginWord])
        backward_queue = collections.deque([endWord])
        backward_set = set([endWord])
        
        distance = 1
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(forward_queue, forward_set, backward_set, word_set):
                return distance
            
            distance += 1
            if self.extend_queue(backward_queue, backward_set, forward_set, word_set):
                return distance
            
        return 0
    
    def extend_queue(self, queue, visited, target_set, word_set):
        for _ in range(len(queue)):
            word = queue.popleft()
            for next_word in self.get_next_words(word, word_set):
                if next_word in visited:
                    continue
                if next_word in target_set:
                    return True
                queue.append(next_word)
                visited.add(next_word)
        return False
    
    def get_next_words(self, word, word_set):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[i]:
                    continue
                new_word = left + char + right
                if new_word in word_set:
                    words.append(new_word)
        return words
                