class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            hashmap[self.create_rep(string)].append(string)
        
        result = []
        for key, value in hashmap.items():
            result.append(value)

        return result
    
    def create_rep(self, string):
        key = [0]*26
        for char in string:
            key[ord(char)-ord('a')] += 1
        
        return tuple(key)