class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        biggest_positive = 0
        biggest_negative = 0

        for number in nums:
            if number > biggest_positive:
                for value in nums:
                    if value == -number:
                        biggest_positive = number
                        biggest_negative = value
           

        for i in range(len(nums)):
            if nums[i] == -biggest_negative and nums[i]!=0:
                return nums[i]
        return -1