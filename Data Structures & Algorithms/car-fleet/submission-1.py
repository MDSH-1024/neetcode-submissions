class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = {}
        for i, pos in enumerate(position):
            car[pos] = speed[i]

        position.sort()
        times = []
        for pos in position:
            times.append((target-pos)/car[pos])
        stack = []
        for time in times:
            while stack and time >= stack[-1] :
                stack.pop()
            
            stack.append(time)
        

        return len(stack)