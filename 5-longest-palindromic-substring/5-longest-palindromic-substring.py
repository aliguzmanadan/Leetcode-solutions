#returns largest string
def longestString(s1, s2):
    if len(s1) < len(s2):
        return s2
    else: 
        return s1
    
    
#Check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]
    
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        tail = 0
        largestPalindrome = s[0]

        for i in range(1, len(s)):
            if s[i] == s[tail-1] and tail != 0:
                tail = tail - 1
            else:
                for j in range(tail, i+1):
                    if is_palindrome(s[j:i+1]):
                        tail = j
                        break

            largestPalindrome = longestString(largestPalindrome, s[tail:i+1])

        return largestPalindrome
                
            
            