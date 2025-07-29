class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1 = len(str1)
        length2 = len(str2)

        def isDivisor(length):
            if length1 % length or length2 % length:
                return False
            factor1 = length1 // length
            factor2 = length2 // length

            return str1[:length] * factor1 == str1 and str1[:length] *factor2 == str2

        for length in range(min(length1, length2), 0, -1):
            if isDivisor(length):
                return str1[:length]
        return ""

