class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        freq_t={}
        if len(s)!=len(t):
            return False
        for c in s:
            freq_s[c]=freq_s.get(c,0)+1
        for c in t:
            if c in freq_s:
                freq_s[c]-=1
                if freq_s[c]<0:
                    return False
            else:
                return False
        return True
        