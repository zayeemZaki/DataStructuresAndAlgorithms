class Solution:
    def moveZeroes(self, nums: list) -> None:

        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1
            
            fast += 1

        return nums