class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                t, i = stack[-1]
                res[i] = index - i
                stack.pop()
            
            stack.append((temperature, index))
            
        return res
            
