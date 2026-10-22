class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i,num in enumerate(nums):
            if num == nums[i-1] and i > 0:
                continue
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                if num + nums[p1] + nums[p2] > 0:
                    p2 -= 1
                elif num + nums[p1] + nums[p2] < 0:
                    p1 += 1
                else:
                    mini_answer = [num,nums[p1],nums[p2]]
                    if mini_answer not in answer:
                        answer.append(mini_answer)
                    p1 += 1
                    p2 -= 1
        return answer