class Solution:
    def isValid(self, s: str) -> bool:
        pairing = {")": "(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in pairing.values():
                stack.append(char)
            else:
                pair = pairing[char]
                if stack:
                    item = stack.pop()
                    if item != pair:
                        return False
                else:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False