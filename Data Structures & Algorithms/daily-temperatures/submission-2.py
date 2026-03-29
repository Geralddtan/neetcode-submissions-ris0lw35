class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, temperature in enumerate(temperatures):
            if not stack:
                stack.append((index,temperature))
                continue
            
            while stack and temperature > stack[-1][1]:
                val = stack.pop()
                res[val[0]] = index-val[0]
            
            stack.append((index,temperature))
        return res
