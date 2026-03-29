class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            key = self.construct_immutable_key(string)
            dic[key].append(string)

        result = []
        for key, value in dic.items():
            result.append(value)
        
        return result

    def construct_immutable_key(self, string):
        key = [0] * 26
        for char in string:
            index = ord(char) - ord('a')
            key[index] += 1
        return tuple(key)
