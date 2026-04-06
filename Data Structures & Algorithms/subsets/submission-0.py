class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for num in nums:
            current_ans_size = len(ans)
            for i in range(current_ans_size):
                currentSet = ans[i]
                new_subset = currentSet[:] 
                new_subset.append(num)
                ans.append(new_subset)
        return ans