import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_s = ""
        reversed_s = ""
        for char in s.lower():
            if re.search("[a-z0-9]", char):
                final_s += char
                reversed_s = char + reversed_s
        return final_s == reversed_s
