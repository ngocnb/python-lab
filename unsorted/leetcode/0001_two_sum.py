from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    number_map = {}

    # build a dict of numbers their index
    for i in range(len(nums)):
        number_map[nums[i]] = i

    for i in range(len(nums)):
        # find the complement of target from num
        num = nums[i]
        complement = target - num

        # check the complement is in the dict or not
        if complement in number_map and number_map[complement] != i:
            return [i, number_map[complement]]

    return []
