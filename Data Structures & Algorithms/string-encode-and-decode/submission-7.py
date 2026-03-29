class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        index = 0
        while index < len(s):
            index_end = index
            while s[index_end] != "#":
                index_end+=1
            length = int(s[index:index_end])
            res.append(s[index_end+1:index_end+1+length])
            index = index_end + 1 + length
        return res
