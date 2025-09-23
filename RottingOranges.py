from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            if queue:
                minutes += 1
        return minutes if fresh == 0 else -1


# Approach 1
# before doing my bfs
# i need to make sure there are no safe oranges
# BFS -> recursively
# def bfs(grid, current_time):
#   return current_time if all oranges are rotten
#   otherwise
#   go through the grid and mark all the 
#   4dir adjacent oranges as rotten
#   bfs(grid, current_time)

# Appraoch 2
# do bfs
# once the bfs terminates, then check if we have
# any remaining 1s in the grid

"""
input = [
        [1, 1, 2, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [2, 0, 0, 1]
        ]
"""