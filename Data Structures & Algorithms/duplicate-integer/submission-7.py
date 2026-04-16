class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_ints=set()

        if len(nums)==0:
            return False

        for num in nums:
            uniq_ints.add(num)
        
        if len(nums)>len(uniq_ints):
            return True
        
        return False
        