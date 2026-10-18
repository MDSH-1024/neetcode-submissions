class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        result = [0] * len(temperatures)
        stack = []

        for i, num in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < num:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)


        return result        