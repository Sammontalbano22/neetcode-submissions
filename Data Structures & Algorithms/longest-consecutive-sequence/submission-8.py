class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        maxcount = 1  
        currcount = 1
        sortedlist = sorted(set(nums))  
        if len(sortedlist) == 1:
            return 1
        
        for i in range(len(sortedlist) - 1):
            if sortedlist[i+1] == sortedlist[i] + 1:  
                currcount += 1
                maxcount = max(maxcount, currcount)
            else:
                currcount = 1 
        
        return maxcount
