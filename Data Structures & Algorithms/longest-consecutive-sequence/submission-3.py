class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_2 = set(nums)
        leng_max = 1
        for i in nums_2:
            if i - 1 not in nums_2:
                leng = 1
                while i + 1 in nums_2:
                    leng += 1
                    i += 1
                    if leng_max < leng:
                        leng_max = leng
        return leng_max

        