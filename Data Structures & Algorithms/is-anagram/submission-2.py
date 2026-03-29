class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        if len(s) != len(t):
            return False
        
        for index in range(len(s)):
            count[ord(s[index]) - ord('a')] += 1
            count[ord(t[index]) - ord('a')] -= 1
        
        for value in count:
            if value != 0:
                return False
        
        return True