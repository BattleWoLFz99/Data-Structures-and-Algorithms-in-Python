from typing import (
    List,
)

class Solution:
    """
    @param score: When the j-th driver gets the i-th order, we can get score[i][j] points.
    @return: return an array that means the array[i]-th driver gets the i-th order.
    """
    def order_allocation(self, score: List[List[int]]) -> List[int]:
        # write your code here
        if not score:
            return

        result = {'max_score':0, 'drivers': None}
        visited = set()
        self.dfs(score, visited, 0, 0, [], result)

        return result['drivers']

    def dfs(self, score, visited, job, curr_score, order, result):
        if len(order) == len(score):
            if curr_score > result['max_score']:
                result['max_score'] = curr_score
                for i in range(len(result)):
                    result['drivers'] = list(order)
            return

        for driver in range(len(score[job])):
            if driver in visited:
                continue
            order.append(driver)
            visited.add(driver)
            self.dfs(score, visited, job + 1, 
                curr_score + score[job][driver], order, result)
            visited.remove(driver)
            order.pop()
