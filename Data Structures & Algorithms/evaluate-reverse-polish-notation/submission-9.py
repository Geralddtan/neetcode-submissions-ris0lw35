class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+","-","*","/"]:
                first = stack.pop()
                second = stack.pop()
                val = eval(str(second)+token+str(first))
                stack.append(int(val))
            else:
                stack.append(token)
        total = int(stack.pop())
        return total