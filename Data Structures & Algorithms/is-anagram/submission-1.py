class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        #return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        dic1 = {}
        dic2 = {}
        for index in range(len(s)):
            dic1[s[index]] = 1 + dic1.get(s[index], 0)
            dic2[t[index]] = 1 + dic2.get(t[index], 0)

        for key, value in dic1.items():
            if key not in dic2 or dic2[key] != value:
                return False
        return True

        
        