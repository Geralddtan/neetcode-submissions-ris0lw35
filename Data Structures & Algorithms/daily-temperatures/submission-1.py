class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]

        for index, temperature in enumerate(temperatures):
            if not stack:
                stack.append((index, temperature))
                continue
            while stack and temperature > stack[-1][1]:
                val = stack.pop(-1)
                result[val[0]] = index - val[0]
            stack.append((index, temperature))

        return result  
            