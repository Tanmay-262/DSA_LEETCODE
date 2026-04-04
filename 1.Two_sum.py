class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # this dict is going to store the value and index
        for i, n in enumerate(nums):#this just puts the value & index in dict
            diff = target - n #logic diff+n = target
            if diff in hash_map:#this checks if the value is already stored
                return [hash_map[diff], i]#this is to display if it exists with the index
            hash_map[n] = i#and in the end hashmap is again assigned a new value
