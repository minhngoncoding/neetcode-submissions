class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashing = set()

        for num in nums:
            if num not in hashing:
                hashing.add(num)
            else:
                return True
        return False