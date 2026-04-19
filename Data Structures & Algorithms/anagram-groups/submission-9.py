class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            key = self.generate_key(string)
            hashmap[key].append(string)

        return list(hashmap.values())

    def generate_key(self, string):
        key = [0] * 26
        for char in string:
            index = ord(char) - ord('a')
            key[index] += 1
        return tuple(key)