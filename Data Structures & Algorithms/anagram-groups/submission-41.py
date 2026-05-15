class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #a dict which the key is the letter freq list, 
        #and the value is the list of the anagrams
        anagrams_freq_dict = {}

        for str in strs:
            freq = [0] * 26
            for char in str:
                
                freq[ord(char) - ord('a')] += 1
            
            freq_tuple = tuple(freq)

                
            if(anagrams_freq_dict.get(freq_tuple) is not None):
                anagrams_freq_dict.get(freq_tuple).append(str)
            else:
                anagrams_freq_dict[freq_tuple] = [str]

        
            
        return list(anagrams_freq_dict.values())

        