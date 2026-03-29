class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for words in strs:
            characters = [0]*26
            for char in words:
                characters[ord(char)-ord('a')] += 1
            dic[tuple(characters)].append(words)
        return dic.values()