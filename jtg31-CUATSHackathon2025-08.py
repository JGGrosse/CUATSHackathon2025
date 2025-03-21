class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {num: 0 for num in nums}

        for num in nums:
            hashmap[num] += 1

        for val in hashmap.values():
            if val != 1:
                return True
        return False 
