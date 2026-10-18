class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [[-1,0]]
        area = 0
        max_area = 0

        for i,num in enumerate(heights):
            while stack and stack[-1][1] > num:
                height = stack.pop()
                area = height[1]*(i - stack[-1][0] - 1)
                if max_area < area:
                    max_area = area
            stack.append([i,num])
        

        return max_area
                
            
