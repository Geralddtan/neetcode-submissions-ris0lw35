class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # s = "".join(filter(str.isalnum, s))
        s = "".join([char for char in s if char.isalnum()])
        front, end = 0, len(s)-1
        while front < end:
            if s[front] != s[end]:
                return False
            front += 1
            end -= 1
        return True