class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = []
        for pos, sp in cars:
            time = (target - pos) / sp
            stack.append(time)
            if len(stack) >=2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)