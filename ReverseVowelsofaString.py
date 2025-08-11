class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}

        input_vowels = []

        for char in reversed(s):
            if char in vowels:
                input_vowels.append(char)

        s_list = list(s)

        for index in range(len(s_list)):
            if s_list[index] in vowels:
                s_list[index] = input_vowels.pop(0)
 
        return "".join(s_list)

        # Travese the input string in reverse order char by char
        #   store the vowels
        # Traverse the input string in regular order char by char
        #   replace each vowel with the first vowel in the stored vowels
        #   pop each vowel out of the stored vowels