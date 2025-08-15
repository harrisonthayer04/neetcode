class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_counts = {}
        word2_counts = {}

        for character in word1:
            if character in word1_counts:
                word1_counts[character] += 1
            else:
                word1_counts[character] = 1
        for character in word2:
            if character in word2_counts:
                word2_counts[character] += 1
            else:
                word2_counts[character] = 1
        if word1_counts.keys() != word2_counts.keys() or sorted(word1_counts.values()) != sorted(word2_counts.values()):
            return False
        return True
        

# 2 Possible Operations 
# 1. Two two existing characters
# 2. Transform all of one character into another


# input: word1 = "abc"
#        word2 = "bca"


# if the strings are the same size:
#   while word1 != word2:
#       do some operations
# else:
#   return false 

# If both strings have the same number of each letter
# then some number of swaps should get us string1 == string2


# Input: word1 = "cabbba", word2 = "abbccc"
# word1_counts = {"a":2, "b"3:,"c":1}
# word2_counts = {"a":1, "b"2:,"c":3}

# for character, count in word1_counts:
#   if count exists in word2_counts:
#       pop it
