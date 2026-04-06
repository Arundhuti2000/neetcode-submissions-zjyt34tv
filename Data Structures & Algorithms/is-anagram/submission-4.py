class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_s= defaultdict(int)
        for char in s:
            freq_s[char]+=1
        for char in t:
            if char in freq_s:
                freq_s[char]-=1
                if freq_s[char]<0:
                    return False
            else:
                return False
        return True 
        