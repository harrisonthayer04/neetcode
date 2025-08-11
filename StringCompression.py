# Solution is written by GPT-5

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        write_index = 0
        read_index = 0
        n = len(chars)

        while read_index < n:
            group_char = chars[read_index]
            group_start = read_index

            # Advance read_index to consume the full group of the same char
            while read_index < n and chars[read_index] == group_char:
                read_index += 1

            group_count = read_index - group_start

            # Write the character
            chars[write_index] = group_char
            write_index += 1

            # Write the count if > 1, digit by digit
            if group_count > 1:
                for digit in str(group_count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index

            
def main():
    # Test Case #1
    input_1 = ["a","a","b","b","c","c","c"]
    k1 = Solution().compress(input_1)
    print(k1)
    print(input_1[:k1])
    print("\n")

    # Test Case #2
    input_2 = ["a"]
    k2 = Solution().compress(input_2)
    print(input_2[:k2])
    print(k2)
    print("\n")

    # Test Case #3
    input_3 = ["a", "a", "a", "a"]
    k3 = Solution().compress(input_3)
    print(input_3[:k3])
    print(k3)
    print("\n")

    # Test Case #4
    input_4 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    k4 = Solution().compress(input_4)
    print(input_4[:k4])
    print(k4)
    print("\n")

if __name__ == "__main__":
    main()

# Possible strategy is to first loop over the input and add 0s
