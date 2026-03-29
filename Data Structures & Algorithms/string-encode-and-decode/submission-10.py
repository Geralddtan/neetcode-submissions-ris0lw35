class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            l, r = index, index
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            word = s[r+1:r+1+length]
            res.append(word)
            index = r+1+length
        
        return res

