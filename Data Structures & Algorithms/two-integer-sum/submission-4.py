from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = defaultdict(int) # val : index
        for i, num in enumerate(nums):
            difference = target - num
            if difference in prev_map:
                return [prev_map[difference], i]
            prev_map[num]=i
        print(num_map)


                


                
        