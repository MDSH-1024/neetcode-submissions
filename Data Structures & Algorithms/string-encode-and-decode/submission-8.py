class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            a = len(word)
            answer += str(a) + "#" + str(word)
        return answer

    def decode(self, s: str) -> List[str]:
        answer = []
        num = 1
        while num <= len(s):
           num_2 = num
           while num_2 <= len(s) and s[num_2] != "#":
                num_2 += 1
           leng = int(s[num - 1:num_2])
           answer.append(s[num_2 + 1 : num_2 + 1 + leng])
           num = num_2 + leng + 2
        return answer
