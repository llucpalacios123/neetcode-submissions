class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums: 
            seen[i] = seen.get(i, 0) + 1
        
        seen = dict(sorted(seen.items(), key=lambda x: x[1], reverse=True))

        lista_final = []

        for i in list(seen)[:k]:
             lista_final.append(i)
        return lista_final
