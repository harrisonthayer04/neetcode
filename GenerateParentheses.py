class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(current: str, open_used: int, close_used: int) -> None:
            if open_used > n or close_used > open_used: return
            if len(current) == n * 2:
                output.append(current)
                return

            backtrack(current + "(", open_used + 1, close_used)
            backtrack(current + ")", open_used, close_used + 1)
        backtrack("", 0, 0)
        return output

# current = "()()"
#             ^ 
# queue = "("

# n pairs of parentheses (well-formed)
#
# brute force:
# generate all possible combinations of the characters "(" and ")"
# then filter out the ones that are invalid
#
# n = 1 -> Generate 2 possible strings
# n = 2 -> Generate 4 possible strings
# Time complexity  O(n^2)
# Space complexity O(n^2)


# Tree style
# backtracking
# recursively
# " ( ( ( (  ) ""
#              ^
