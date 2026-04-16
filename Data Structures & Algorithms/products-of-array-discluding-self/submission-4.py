from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        out_list = []
        zero_count = nums.count(0)
        
        # Calculate the product of all non-zero elements
        if zero_count > 1:
            # If more than one zero, all products will be zero
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                total_product *= num
        
        # Build the output list based on zero presence
        for num in nums:
            if zero_count == 1:
                # If there's exactly one zero, only the position with zero gets total_product
                out_list.append(total_product if num == 0 else 0)
            else:
                # If no zeros, each element is the total product divided by the current element
                out_list.append(total_product // num)
        
        return out_list
