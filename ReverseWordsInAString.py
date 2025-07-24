class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = ""

        for char in s:
            if char != " ":
                word += char
            elif word:
                stack.append(word)
                word = ""
        
        if word:
            stack.append(word)
        return " ".join(reversed(stack))



