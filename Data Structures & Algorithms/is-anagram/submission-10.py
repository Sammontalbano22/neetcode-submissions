class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freq={}
        t_freq={}


        # base_case

        if len(s)!= len(t):
            return False

        
        for let in s:
            if let in s_freq:
                s_freq[let]+=1
            else:
                s_freq[let]=1

        for let in t:
            if let in t_freq:
                t_freq[let]+=1
            else:
                t_freq[let]=1

        return t_freq==s_freq
        