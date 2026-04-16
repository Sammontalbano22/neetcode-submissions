class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_ints=set()

        if len(nums)==0:
            return False

        for num in nums:
            if num in uniq_ints:
                return True
            uniq_ints.add(num)
                
        return False
        