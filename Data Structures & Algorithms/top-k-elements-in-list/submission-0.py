class Solution:
    def quicksort(self,arr: List[int], counts: dict):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if counts[x] > counts[pivot]]
        middle = [x for x in arr if counts[x] == counts[pivot]]
        right = [x for x in arr if counts[x] < counts[pivot]]
        return self.quicksort(left, counts) + middle + self.quicksort(right, counts)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        result=[]
        i=0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        array=list(counts.keys())
        sorted_array = self.quicksort(array,counts)
        return sorted_array[:k]