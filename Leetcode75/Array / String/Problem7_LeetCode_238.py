class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        leftPrefix = [1] * len(nums)
        rightPrefix = [1] * len(nums)

        for i in range(1, len(nums)):
            leftPrefix[i] = leftPrefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            rightPrefix[i] = rightPrefix[i+1] * nums[i+1]

        res = [1] *len(nums)

        for i in range(len(nums)):
            res[i] = leftPrefix[i] * rightPrefix[i]

        return res