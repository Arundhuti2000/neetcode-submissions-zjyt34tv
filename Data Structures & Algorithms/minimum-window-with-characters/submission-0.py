class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        right=0
        window_counts={}
        t_dict={}
        have=0
        for char in t:
            t_dict[char]=t_dict.get(char,0)+1
        need=len(t_dict)
        res = (float('inf'), 0, 0)
        while right<len(s):
            char=s[right]

            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_dict:
                if window_counts[char] == t_dict[char]:
                    have+=1
            
            while have == need:
                current_len=right-left+1
                if res[0]>current_len:
                    res = (current_len, left, right)
                charleft=s[left]
                window_counts[charleft]-=1
                if charleft in t_dict and window_counts[charleft] < t_dict[charleft]:
                    have-=1
                left += 1
            right+=1
        if res[0] == float('inf'):
            return ""
        else:
            return s[res[1] : res[2] + 1]