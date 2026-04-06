from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        max_length=0
        left = 0
        right = 0
        count_length=0
        seen= set()
        #abcabbac
        while right<=n-1:
            # if count_length>max_length:
            #     max_length = count_length   
            if s[right] in seen:
                seen.remove(s[left])
                left+=1
            else:
                seen.add(s[right])
                max_length = max(max_length,right- left + 1)
                right+=1
                # count_length+=1  
        return max_length
            