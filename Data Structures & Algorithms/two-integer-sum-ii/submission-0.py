
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checker = False
        solset = set(numbers)  # Used for quick lookups
        stored_ind1 = 0
        stored_ind2 = 0
        indvalue = 0
        
        for i in range(len(numbers) - 1):
            indvalue = target - numbers[i]
            if indvalue in solset:  # Check if complement exists
                checker = True
                stored_ind1 = i + 1  # 1-indexed
        
                for j in range(i + 1, len(numbers)):  # Start after i
                    if numbers[j] == indvalue:
                        stored_ind2 = j + 1  # 1-indexed
                        break  # Stop when we find the first match
                
                break  # We only need one valid pair
        
        return [stored_ind1, stored_ind2] if stored_ind1 < stored_ind2 else [stored_ind2, stored_ind1]