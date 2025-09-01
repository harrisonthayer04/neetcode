class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            self.visited.add(i)
            for j in range(0, n):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)
            return

        province = 0
        self.visited = set()
        n = len(isConnected)
        for i in range(0, n):
            if i not in self.visited:
                province += 1
                dfs(i)
        return province


# Connect all the cities
# Buckets of cities
#
# 1 1 0 1
# 1 1 0 1
# 0 0 1 0
# 1 1 0 1
#
#
#
#
#
