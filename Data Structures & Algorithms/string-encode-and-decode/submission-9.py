class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "#" 
            res += string
        return res

    "5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            start_index = j+1
            i, j = start_index, start_index + length
            res.append(s[i:j])
            i = j
        return res
            

