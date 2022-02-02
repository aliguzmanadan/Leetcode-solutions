def is_palindrome(s):
    return s == s[::-1]

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = set()
        
        dict_words = {word[::-1]:i for i,word in enumerate(words)}

        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]

                if is_palindrome(prefix) and suffix in dict_words and i != dict_words[suffix]:
                    answer.add((dict_words[suffix], i))
                if is_palindrome(suffix) and prefix in dict_words and i != dict_words[prefix]:
                    answer.add((i, dict_words[prefix]))

        return [list(p) for p in answer]