class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        for i in range(len(s)):
            l, r = i, i
            palin = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin = s[l:r+1]
                l-=1
                r+=1
            if len(palin) > len(res):
                res = palin

        for i in range(len(s)):
            l, r = i, i+1
            palin = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin = s[l:r+1]
                l-=1
                r+=1
            if len(palin) > len(res):
                res = palin    

        return res

