class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash nums into a map
            # key: value
            # value: index
        index_map = {}
        for index, value in enumerate(nums):
            index_map[value] = index
    
        for index, item in enumerate(nums):
            comp = target - item
            if comp in index_map and index_map[comp] != index:
                return [index, index_map[comp]]