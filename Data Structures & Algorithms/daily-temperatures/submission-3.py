class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append([index, temp])
                continue
            
            while stack and temp > stack[-1][1]:
                prev_index, _ = stack.pop()
                res[prev_index] =  index-prev_index

            stack.append([index, temp])
        
        return res


