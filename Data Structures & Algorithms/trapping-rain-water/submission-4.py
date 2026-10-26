class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0 
        p2 = len(height) - 1
        answer = [0]*len(height)
        left_max = 0
        right_max = 0

        while p1 < p2:
            if left_max < height[p1]:
                left_max = height[p1]
            if right_max < height[p2]:
                right_max = height[p2]

            water = min(left_max, right_max) - height[p1]
            if water > 0:
                answer[p1] = water
            
            water = min(left_max, right_max) - height[p2]
            if water > 0:
                answer[p2] = water

            
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
            

        return sum(answer)
