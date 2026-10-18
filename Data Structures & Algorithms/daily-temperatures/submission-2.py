class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        result = [0] * len(temperatures)
        stack = []

        for i, num in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < num:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i
                
            
            stack.append(i)


        return result        