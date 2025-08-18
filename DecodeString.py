class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for index in range(0, len(s)):
            if s[index] != "]":
                stack.append(s[index])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substring)
        return "".join(stack)