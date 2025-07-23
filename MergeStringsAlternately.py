class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longest = len(word1) if len(word1) > len(word2) else len(word2)
        output = ""
        for i in range(0, longest):
            if i < len(word1):
                output += word1[i]
            if i < len(word2):
                output += word2[i]
        return output
        


# Soln 1:
# Loop over the length of the longest word
# word1 = abc
# word2 = 12345




