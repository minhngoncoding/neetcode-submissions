class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashing = {}

        for num in nums:
            if num not in hashing:
                hashing[num] = 0
            else:
                return True

        return False