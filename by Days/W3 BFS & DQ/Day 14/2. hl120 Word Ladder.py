# 不分层 直接 pop。需要用 dict
class Solution:
    def ladderLength(self, start, end, dict):
        if not dict:
            return None

        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}

        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
            for next_word in self.get_next_words(word, dict):
                if next_word in distance:
                    continue
                distance[next_word] = distance[word] + 1
                queue.append(next_word)

        return 0

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                next_word = left + char + right
                if next_word in dict:
                    words.append(next_word)

        return words


# 分层，保留层次信息。分层的话统一模板，把判断 == end 扔到下面给 next
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        # 找不到返回 0，一次变换返回2，所以这里初始化为 1
        distance = 1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                for next_word in self.get_next_words(word, dict):
                    if next_word in visited:
                        continue
                    if next_word == end:
                        return distance
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    def get_next_words(self, word, dict):
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                new_word = left + char + right
                if new_word in dict:
                    next_words.append(new_word)
        return next_words

