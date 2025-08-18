class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for character in s:
            if character == "*":
                if output:
                    output.pop()
            else:
                output.append(character)
        return "".join(output)