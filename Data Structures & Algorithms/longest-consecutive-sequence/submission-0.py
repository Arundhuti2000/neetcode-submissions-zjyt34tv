class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen=0
        count_set=set(nums)
        for num in count_set:
            if (num-1) not in count_set:
                cur_num=num
                cur_len=1
                while (cur_num +1 ) in count_set:
                    cur_num+=1
                    cur_len+=1
                maxLen=max(maxLen,cur_len)
        return maxLen