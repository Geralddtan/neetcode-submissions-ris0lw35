class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for index, val in enumerate(position):
            time_taken = (target-val)/speed[index]
            cars.append([val, time_taken])

        cars.sort(key = lambda x:x[0])
        for car in cars:
            stack.append(car)

        ref = None
        res = 0
        while stack:
            ref = stack.pop()
            res += 1
            time_taken = ref[1]
            while stack and stack[-1][1] <= time_taken:
                stack.pop()

        return res

