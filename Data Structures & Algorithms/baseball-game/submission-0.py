class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1]*2)
            elif operation == "+":
                val1 = stack[-1]
                val2 = stack[-2]
                stack.append(val1+val2)
            else:
                stack.append(int(operation))

        res = 0
        for value in stack:
            res += value
        
        return res