class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_s = {}
        for _ in s:
            freq_s[_]= freq_s.get(_, 0) +1
        for _ in t:
            if _ in freq_s:
                freq_s[_]-=1
                if freq_s[_]<0:
                    return False
            else:
                return False
        return True
        