# prefix_to_words
class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
             we will sort your return value in output
    """
    def word_squares(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []

        squares = []
        prefix_to_words = self.get_prefix_to_words(words)
        for word in words:
            self.dfs(words, prefix_to_words, [word], squares)
        return squares

    def dfs(self, words, prefix_to_words, square, squares):
        n = len(square)
        if n == len(words[0]):
            squares.append(list(square))
            return

        prefix_list = []
        for i in range(n):
            prefix_list.append(square[i][n])
        prefix = ''.join(prefix_list)
        # prefix = ''.join([square[i][n] for i in range(n)])
        for word in prefix_to_words.get(prefix, []):
            square.append(word)
            self.dfs(words, prefix_to_words, square, squares)
            square.pop()

    def get_prefix_to_words(self, words):
        prefix_to_words = {}
        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_to_words:
                    prefix_to_words[prefix] = []
                prefix_to_words[prefix].append(word)
        return prefix_to_words


# Pruning
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []
        
        prefix_to_words = self.get_prefix_to_words(words)
        squares = []
        for word in words:
            self.dfs(words, prefix_to_words, [word], squares)
        
        return squares
    
    def dfs(self, words, prefix_to_words, square, squares):
        curr_index = len(square)
        if curr_index == len(words[0]):
            squares.append(list(square))
            return
        
        for row_index in range(curr_index + 1, len(words[0])):
            prefix = ''.join([square[i][row_index] for i in range(curr_index)])
            if prefix not in prefix_to_words:
                return
        
        prefix = ''.join([square[i][curr_index] for i in range(curr_index)])
        for word in prefix_to_words.get(prefix, []):
            square.append(word)
            self.dfs(words, prefix_to_words, square, squares)
            square.pop()
        
    def get_prefix_to_words(self, words):
        prefix_to_words = {}
        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_to_words:
                    prefix_to_words[prefix] = []
                prefix_to_words[prefix].append(word)
                
        return prefix_to_words
            