from collections import defaultdict

def delete_if_zero(dic, char):
    if dic[char] == 0:
        dic.pop(char)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        freq = defaultdict(int) 
        answer = []

        for char in p:
            freq[char] += 1

        for char in s[:len(p)]:
            freq[char] -= 1
            delete_if_zero(freq, char)

        if not freq:
            answer.append(0)

        for i in range(1, len(s)-len(p)+1):
            freq[s[i-1]] += 1
            delete_if_zero(freq, s[i-1])
            freq[s[i+len(p)-1]] -= 1
            delete_if_zero(freq, s[i+len(p)-1])

            if not freq:
                answer.append(i)

        return answer