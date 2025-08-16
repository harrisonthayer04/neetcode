class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = {}
        for number in arr:
            if number in frequencies:
                frequencies[number] += 1
            else:
                frequencies[number] = 1
        return (len(frequencies.values()) == len(set(frequencies.values())))
