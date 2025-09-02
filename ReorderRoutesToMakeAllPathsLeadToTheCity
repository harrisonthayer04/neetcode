class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbors
        # count outgoing edges

        edges = {(a,b) for a, b in connections} # add each connection to a hash set
        neighbors = { city:[] for city in range(n)} # create an empty list for each cities neighbors
        visit = set() # keep track of visited nodes for optimal complexity
        changes = 0 # final return

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            for neighbor in neighbors[city]:
                if neighbor in visit: continue
                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes


# connections = [[0,1],[3,1],[2,3],[4,0],[4,5]]

# 
# def dfs():
#
# how do i determine if a given edge breaks the path
# map = {0:true, 1:true, 2:false, 3:true, 4:true , 5:false}
#
#
#
