class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        if len(rooms[0]) == 0 and len(rooms) != 1:
            return False
        
        queue = collections.deque([0])
        visited = set([0])
        while queue:
            room = queue.popleft()
            for next_room in rooms[room]:
                if next_room in visited:
                    continue
                queue.append(next_room)
                visited.add(next_room)
        
        return len(visited) == len(rooms)