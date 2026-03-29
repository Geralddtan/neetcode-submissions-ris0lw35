class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            nonlocal subset
            if i >= len(s):
                res.append(subset.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
            
            return
        
        dfs(0)
        return res

    def isPalindrome(self, orig, i, j):
        s = orig[i:j+1]
        if s == s[::-1]:
            return True
        return False
