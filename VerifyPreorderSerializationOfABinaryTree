class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for character in preorder.split(","):
            stack.append(character)
            while len(stack) > 2 and stack[-2:] == ["#", "#"] and stack[-3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return stack == ["#"]

