class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(stack, openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
                return
            if openP < n:
                stack.append("(")
                backtrack(stack.copy(), openP+1, closedP)
                stack.pop()
            if closedP < openP:
                stack.append(")")
                backtrack(stack.copy(),openP, closedP+1)
                stack.pop()

        backtrack([],0,0)
        return res

