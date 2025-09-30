class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case: if digits is empty return an empty list
        if not digits: return []
        # create a dictionary that maps the digits to the letters
        numbers = {
            '2': 'abc','3': 'def',
            '4': 'ghi','5': 'jkl',
            '6': 'mno','7': 'pqrs',
            '8': 'tuv','9': 'wxyz'
        }
        # maintain a result array
        result = []
        # helper/recursive function that takes in an index and a path string
        def backtrack(index: int, path: str) -> None:
            # when the index is the length of digits,
            # append the combination and return
            if index == len(digits):
                result.append(path)
                return
            # extract the needed digit
            current_digit = digits[index]
            letters = numbers[current_digit]

            for letter in letters: backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result

# 2 to 9
# 2,3,4
#       2       2      2
#     3 3 3   3 3 3  3 3 3