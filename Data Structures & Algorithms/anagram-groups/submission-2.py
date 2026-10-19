class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapFinal = {}

        for i in strs:
            freqWords = [0] * 26
            for j in i: 
                indice = ord(j) - ord('a')
                freqWords[indice] += 1
            
            if tuple(freqWords) not in mapFinal:
                mapFinal[tuple(freqWords)] = []
                
            mapFinal[tuple(freqWords)].append(i)
    
        return list(mapFinal.values())
                
