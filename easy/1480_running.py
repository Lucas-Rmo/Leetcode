class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        value = 0
        list_values = []
        for i in range(len(nums)):
            value = nums[i]
            for j in range(i):
                value += nums[j]

            list_values.append(value)
            value = 0

        return list_values
