class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict={}
        for item in (nums):
            if item not in freqdict:
                freqdict[item]=1
            else:
                freqdict[item]+=1
        max_value=0
        tupkey=(0,0)

        kfreq=[]
        for i in range(k):
            max_value_pair=(None,0)
            for key, value in freqdict.items():
                if value>max_value_pair[1]:
                    max_value_pair= (key,value)
            kfreq.append(max_value_pair[0])
            del freqdict[max_value_pair[0]]
        return kfreq
                    
                
                


            
            



        