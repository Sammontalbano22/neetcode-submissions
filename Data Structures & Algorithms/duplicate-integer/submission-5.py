class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets=set()

        if len(nums)==0:
            return False

        for num in nums:
            sets.add(num)

        if len(nums)>len(sets):
            return True
        
        
        return False




        


       

    