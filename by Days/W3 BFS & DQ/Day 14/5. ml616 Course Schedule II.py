class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # 初始化可BFS的图
        # graph 不能写成 [[]] * numCourses，会报错
        # 这里写成 list 下标作为 course 访问
        # dict 看 127 node_to_indegree = {x:0 for x in graph}
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        # 1. 建图(统计每个点的入度)
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1

        # 2. 将入度为 0 的编号加入队列
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # 记录
        order = []
        course_taken = 0


        while queue:
            # 3. 不断的从队列中拿出一个点，去掉连边，对应点入度 -1
            curr = queue.popleft()
            order.append(curr)
            course_taken += 1
            for next_course in graph[curr]:
                in_degree[next_course] -= 1
                # 4. 有新入度为0，丢回队列
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return order if course_taken == numCourses else []