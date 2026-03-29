class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_ls = defaultdict(list)
        for string in strs:
            count = [0]*26

            for char in string:
                count[ord(char) - ord("a")] += 1

            final_ls[tuple(count)].append(string)
        
        return final_ls.values()
            