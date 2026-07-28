class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #add cars to the stack in position order
        cars = []
        length = len(position)
        for i in range(length):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = []
        for pos, sp in cars:
            time = (target-pos) / sp
            stack.append(time)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)