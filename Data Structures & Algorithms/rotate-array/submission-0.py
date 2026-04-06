class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        k=k%n
        
        nums[:]=nums[-k:] + nums[:-k]
        