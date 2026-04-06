class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        res=[]
        if len(nums) < 3:
            return []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]
                if cur_sum==0:
                    ans.add(tuple([nums[i], nums[left], nums[right]]))
                    left+=1
                    right-=1
                elif cur_sum < 0:
                    left += 1
                else:
                    right-=1
        return [list(triplet) for triplet in ans]
            
                        
        
        