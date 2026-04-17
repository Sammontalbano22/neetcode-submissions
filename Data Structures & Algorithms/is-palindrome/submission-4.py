class Solution:
    def isPalindrome(self, s: str) -> bool:

        fixed = s.lower()
        alpha_fixed = [c for c in fixed if c.isalnum()]

        i = 0
        j = len(alpha_fixed) - 1

        while i < j:
            if alpha_fixed[i] != alpha_fixed[j]:
                return False
            i += 1
            j -= 1

        return True