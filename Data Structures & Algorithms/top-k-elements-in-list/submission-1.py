class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        answer = []
        sorted_seen = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(0, k):
            answer.append(sorted_seen[i][0])
        return answer
