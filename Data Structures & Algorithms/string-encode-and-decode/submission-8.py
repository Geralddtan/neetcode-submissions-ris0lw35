class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"
            res += s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            end_index = index
            while s[end_index] != "#":
                end_index += 1
            length = int(s[index:end_index])
            res.append(s[end_index+1:end_index+1+length])
            index = end_index+1+length
        
        return res



