class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for token in tokens:
            if token in ("+","-","*","/"):
                first = stack.pop()
                second = stack.pop()
                val = int(eval(str(second) + token + str(first)))
                stack.append(val)
            else:
                stack.append(token)

        total = int(stack.pop())
        return total
