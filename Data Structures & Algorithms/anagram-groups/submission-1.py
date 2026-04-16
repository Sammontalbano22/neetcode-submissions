class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        useset = {}
        for item in strs:
            sorted_str = ''.join(sorted(item))
            if sorted_str not in useset:
                useset[sorted_str] = []
            useset[sorted_str].append(item)

        fnal = list(useset.values())
        return fnal
