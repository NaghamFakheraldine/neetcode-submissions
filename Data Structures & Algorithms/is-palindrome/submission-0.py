import re, string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations_pattern = f"[{re.escape(string.punctuation)}]"
        revered_lowered_s = re.sub(punctuations_pattern, '', (''.join((str.lower(s)[::-1].split()))))
        lowered_s = re.sub(punctuations_pattern, '', (''.join((str.lower(s).split()))))
        print(revered_lowered_s, lowered_s)

        return revered_lowered_s == lowered_s
