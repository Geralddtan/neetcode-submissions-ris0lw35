class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            ascii_ls = [0]*26
            for char in string:
                ascii_ls[ord(char) - ord("a")] += 1

            hashmap[tuple(ascii_ls)].append(string)
        
        return list(hashmap.values())
