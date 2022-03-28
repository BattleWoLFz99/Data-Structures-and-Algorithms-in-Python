DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)
        if source == target:
            return 0
        
        queue = collections.deque([(source)])
        distance = {source: 0}
        
        while queue:
            curr_string = queue.popleft()
            if curr_string == target:
                return distance[curr_string]
            for next_string in self.get_next_states(curr_string, final_state):
                if next_string in distance:
                    continue
                queue.append(next_string)
                distance[next_string] = distance[curr_string] + 1
        
        return -1
        
    def matrix_to_string(self, state):
        state_list = []
        for i in range(len(state)):
            for j in range(len(state[0])):
                state_list.append(str(state[i][j]))
                
        return "".join(state_list)
    
    def get_next_states(self, string, final_state):
        n, m = len(final_state), len(final_state[0])
        states = []
        zero_index = string.find('0')
        # 这里用的是 m，一律都是 m ！！
        x, y = zero_index // m, zero_index % m
        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            if not (0 <= next_x < n and 0 <= next_y < m):
                continue
            next_state = list(string)
            next_state[x * m + y] = next_state[next_x * m + next_y]
            next_state[next_x * m + next_y] = '0'
            states.append("".join(next_state))
        
        return states


# 双向 BFS 准备，先改成 分层，统一模板：
# 注意 next 扔下面去了
    def minMoveStep(self, init_state, final_state):
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)
        if source == target:
            return 0
        
        queue = collections.deque([(source)])
        visited = set([(source)])
        distance = 0
        
        while queue:
            # distance 写在这里 然后加上 for
            # == target 扔到下面里去
            # 有个很坑的点是 Word Ladder，找不到返回0，找到了变换一次返回 2
            distance += 1
            for _ in range(len(queue)):
                curr_string = queue.popleft()
                for next_string in self.get_next_states(curr_string, final_state):
                    if next_string in visited:
                        continue
                    if next_string == target:
                        return distance
                    queue.append(next_string)
                    visited.add(next_string)
        
        return -1


# 改双向。是真的容易出BUG，最好给自己5分钟
    def minMoveStep(self, init_state, final_state):
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)
        if source == target:
            return 0
        
        # 1. 双层 queue set
        forward_queue = collections.deque([(source)])
        forward_set = set([(source)])
        backward_queue = collections.deque([(target)])
        backward_set = set([(target)])

        distance = 0
        # 1. 这里跟着一起改，不然很容易忘
        while forward_queue and backward_queue:
            distance += 1
            # 4. 这里要仔细检查，self. 以及 参数有没有更多
            if self.extend_queue(forward_queue, forward_set, backward_set, final_state):
                return distance

            distance += 1
            if self.extend_queue(forward_queue, forward_set, backward_set, final_state):
                return distance

        return -1

    # 2. 分离，记得检查缩进
    def extend_queue(self, queue, visited, target_set, final_state):  
        for _ in range(len(queue)):
            curr_string = queue.popleft()
            for next_string in self.get_next_states(curr_string, final_state):
                if next_string in visited:
                    continue
                # 3. 改 in target_set，同时改 True / False
                if next_string in target_set:
                    return True
                queue.append(next_string)
                visited.add(next_string)
        
        return False