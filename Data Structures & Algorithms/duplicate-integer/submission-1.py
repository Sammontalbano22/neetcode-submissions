class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        use=set(nums)
        if len(use)!=len(nums):
            return True
        return False
         