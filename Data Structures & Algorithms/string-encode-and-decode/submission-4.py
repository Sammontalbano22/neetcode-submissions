class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        if strs==[]:
            return '[]'

        for item in strs:
            encoded_string+= item + "../"
        return encoded_string[:-3]

    def decode(self, s: str) -> List[str]:
        if s=="[]":
            return []
        return s.split("../")
