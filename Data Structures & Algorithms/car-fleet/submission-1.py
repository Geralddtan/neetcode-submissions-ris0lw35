class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(key = lambda x: x[0])
        stack = position_speed
        count = 0
        while stack:
            count += 1
            car = stack.pop()
            time_to_destination = (target - car[0])/car[1]
            while stack and (target - stack[-1][0])/stack[-1][1] <= time_to_destination:
                stack.pop()
        
        return count
