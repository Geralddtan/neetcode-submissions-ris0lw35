class Solution:
    def isAnagram(self, str1, str2) -> bool:
        return sorted(str1) == sorted(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_ls = []
        for string in strs:
            for ls in final_ls:
                if self.isAnagram(string, ls[0]):
                    ls.append(string)
                    break
            else:
                final_ls.append([string])
        return final_ls
            