class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        freq=[[]for i in range(len(nums)+1)]
        result=[]
        i=0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for v, c in counts.items():
            freq[c].append(v)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result