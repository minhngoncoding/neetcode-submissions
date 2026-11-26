class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for index, num in enumerate(nums):
            remain = target - num
            if num not in hashmap:
                hashmap[remain] = index
            else:
                return [hashmap[num], index]
        
