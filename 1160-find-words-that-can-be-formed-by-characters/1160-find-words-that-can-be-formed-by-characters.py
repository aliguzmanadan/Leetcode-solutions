class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
    
        for word in words:
            dummy_chars = chars

            for char in word:
                if char not in dummy_chars:
                    break
                dummy_chars = dummy_chars.replace(char, "", 1)

            if len(dummy_chars) + len(word) == len(chars):
                sum += len(word)

        return sum