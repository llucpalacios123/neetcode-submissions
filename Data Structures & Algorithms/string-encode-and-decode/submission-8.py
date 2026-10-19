class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final += str(len(i)) + "/" + i
        return final

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            slash_index = s.find('/', i)
            length = int(s[i:slash_index])
            start = slash_index + 1
            final.append(s[start:start + length])
            i = start + length
        
        return final