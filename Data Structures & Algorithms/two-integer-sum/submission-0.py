class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= defaultdict(int)
        result=[]
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                result.append(hashmap[diff])
                result.append(i)
                return result
            else:
                hashmap[nums[i]]= i
        else:
            return result
