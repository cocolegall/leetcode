from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}
        n = len(nums)

        for i in range(n) :
            hash_table[nums[i]] = i

        for i in range(n) :
            y = target - nums[i]
            if y in hash_table and hash_table[y] != i :
                return [i,hash_table[y]]