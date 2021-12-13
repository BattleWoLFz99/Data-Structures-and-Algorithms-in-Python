# start 也要输出，别上来就 [], results
# 找最短的所有方案：BFS找最短，DFS找所有

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, d):
        d.add(start)
        d.add(end)

        distance = {}
        from_to_map = {}
        for word in d:
            from_to_map[word] = []
        self.bfs(start, d, distance, from_to_map)

        results = []
        self.dfs(start, end, d, from_to_map, distance[end], [start], results)

        return results

    def bfs(self, start, d, distance, from_to_map):
        queue = collections.deque([start])
        distance[start] = 0
        while queue:
            curr_word = queue.popleft()
            for next_word in self.get_next_words(curr_word, d):
                if next_word not in distance:
                    distance[next_word] = distance[curr_word] + 1
                    from_to_map[curr_word].append(next_word)
                    queue.append(next_word)
                elif distance[next_word] == distance[curr_word] + 1:
                    from_to_map[curr_word].append(next_word)

    def get_next_words(self, word, d):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == c:
                    continue
                next_word = word[:i] + c + word[i+1:]
                if next_word in d:
                    words.append(next_word)

        return words

    def dfs(self, curr_word, end, d, from_to_map, min_step, path, results):
        if curr_word == end:
            results.append(list(path))
            return

        if len(path) > min_step:
            return

        for next_word in from_to_map[curr_word]:
            path.append(next_word)
            self.dfs(next_word, end, d, from_to_map, min_step, path, results)
            path.pop()