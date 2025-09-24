# Import a dequeue
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Store the # of rows, # of columns, # of fresh oranges, and queue
        rows = len(grid) 
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        # Loop is O(n) * O(m)
        # Loop over all the cells in the m x n matrix
        for r in range(0, rows):
            for c in range(0, cols):
                # If the cell contains a 2 -> add it to the queue
                # If the cell contains a 1 -> incremenet the fresh counter
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        # If there are no fresh oranges then we have no steps
        if fresh == 0: return 0

        # Maintain a counter for the number of minutes,
        # also establish all possible directions
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # While there are cells in the queue
        while queue:
            # Loop over all the cells in the queue
            for _ in range(len(queue)):
                # Pop the row and column from the queue
                r, c = queue.popleft()
                # Then loop over the possible directions 
                for dr, dc in directions:
                    # Hold the new possible cell
                    nr, nc = r + dr, c + dc
                    # If the cell we are inspecting is possiblem AND a 1
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Set it to a 2,
                        # decremenet our fresh counter,
                        # append the 2 to our queue
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            # Once done looping, if there is something left in the queue
            # we want to increment minutes
            if queue:
                minutes += 1
        # return minutes if we have infect all fresh oranges
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