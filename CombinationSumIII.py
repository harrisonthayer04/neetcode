class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # List out the possible digits
        possible = [1,2,3,4,5,6,7,8,9]
        # Maintain an array to store solutions
        result = []
        # Decalare our backtacking helper function
        def backtrack(index: int, path: List[int]):
            # base case where if the path is the proper length
            if len(path) == k:
                # and the sum is the desired sum
                if sum(path) == n:
                    # then append a copy of the path to the solution array
                    result.append(path[:])
                # return
                return
            # if the sum of the path is greater than the desired sum, then just return
            if sum(path) > n: return 
            # loop over the indixies from the current index to the length of possible
            for index in range(index, len(possible)):
                # append to the path the current value from possible
                path.append(possible[index])
                # call the recursive helper function
                backtrack(index + 1, path)
                # pop the path
                path.pop()
        # begin the recursion
        backtrack(0, [])  
        # return the array of results  
        return result


# return the possible combinations of k numbers that sum to n
# possible numbers are 1-9

# k = 4, n = 20
# possible = [[], [], [], ...]


#           1,2,3,4,5,6,7,8,9
# 1,2,3,4,5,6,7,8,9
#
#

# def helper(path: List)



# we know there is a minimum solution of 
# 1 + 2 + 3 + 4 = 10
