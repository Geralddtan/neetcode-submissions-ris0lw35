class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(subset, i):
            if i >= len(digits):
                res.append(subset)
                return
            
            for char in digitToChar[digits[i]]:
                backtrack(subset+char, i+1)
        
        if digits:
            backtrack("", 0)

        return res
            


