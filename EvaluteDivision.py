class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for index, value in enumerate(values):
            numerator, denominator = equations[index]
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value
        
        def dfs(node, target, current, visited):
            if (node not in graph or target not in graph): return -1 # Base Cases
            if node == target: return 1
            if target in graph[node]: return current * graph[node][target]
            visited.add(node)
            for connection in graph[node]:
                if connection not in visited:
                    result = dfs(connection, target, current * graph[node][connection], visited)
                    if result != -1: return result
            return -1

        output = []
        for numerator, denominator in queries: output.append(dfs(numerator, denominator, 1, set()))
        return output


# a / b = 2
    # a = 2b
# b / c = 3 
    # b = 3c