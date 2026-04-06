class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        freq_t={}
        if len(s)!=len(t):
            return False
        for c in s:
            freq_s[c]=freq_s.get(c,0)+1
        for c in t:
            freq_t[c]=freq_t.get(c,0)+1
        if freq_s!= freq_t:
            return False
        return True
        