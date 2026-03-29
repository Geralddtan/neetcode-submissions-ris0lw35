class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def dfs(valid, stack, next_brack):
            if next_brack == ")" and len(stack) == 0:
                return
            if len(valid) == 2*n and len(stack) > 0:
                return
            if len(valid) == 2*n:
                final.append(valid)
                return
            else:
                if next_brack == "(":
                    stack.append(next_brack)
                if next_brack == ")":
                    stack.pop()
                
                valid += next_brack
                dfs(valid, stack.copy(), "(")
                dfs(valid, stack.copy(), ")")
                
        dfs("",[],"(")
        return final

