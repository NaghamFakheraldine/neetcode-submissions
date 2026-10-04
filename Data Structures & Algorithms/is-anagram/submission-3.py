class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted_list = sorted(list(s))
        t_sorted_list = sorted(list(t))
        return sorted(list(s)) == sorted(list(t))
