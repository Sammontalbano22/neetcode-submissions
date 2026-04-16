class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freq={}
        t_freq={}


    #Base case
        if len(s) != len(t):
            return False

    # This will create hash tables for each string

        for letter in s:
            if letter in s_freq:
                s_freq[letter]+=1
            else:
                s_freq[letter]=1

        for letter in t:
            if letter in t_freq:
                t_freq[letter]+=1
            else:
                t_freq[letter]=1


    # compare dictionaries

        return s_freq==t_freq
                
      
        