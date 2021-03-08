class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if string is empty, return 0
        if s == '':
            return 0
        
        # if string is a palindrome, one removal
        if s == s[::-1]:
            return 1
        
        # else, one removal on a non palindrome non empty string (with only 2 characters) will return a palindromic string.
        return 2