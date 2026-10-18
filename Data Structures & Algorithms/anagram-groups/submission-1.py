class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for i in strs:
            key = tuple(sorted(i))

            if key not in answer:
                answer[key] = []
            
            answer[key].append(i)
        return list(answer.values())

