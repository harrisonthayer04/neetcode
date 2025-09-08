class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cells = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        rows = len(maze)
        columns = len(maze[0])
        while cells:
            r, c, steps = cells.popleft()
            check = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for i, j in check:
                if i >= 0 and j >= 0 and i < rows and j < columns and maze[i][j] == ".":
                    if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                        return steps + 1
                    cells.append((i, j, steps + 1))
                    maze[i][j] = "+"
        return -1
        

# How to know if we are at an exit
# (x, y) -> if x or y are the largest or smallest possible
# values then we are at an exit
# 

# maze = [["+","+",".","+"],
#         [".",".","S","+"],
#         ["+","+","+","."]]
# entrance = [1,2]
# recursive approach