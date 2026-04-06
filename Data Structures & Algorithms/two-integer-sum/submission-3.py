class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return 0
        hashmap= defaultdict(int)
        result=[]
        for i in range(0,len(nums)):
            expected_j = target - nums[i]
            if expected_j in hashmap:
                result.append(hashmap[expected_j])
                result.append(i)
                return result
            else:
                hashmap[nums[i]]=i
#storing the values as keys as the indexes as values