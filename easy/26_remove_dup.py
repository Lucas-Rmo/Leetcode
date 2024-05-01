class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_nums = []
        for value in nums:
            if value not in new_nums:
                new_nums.append(value)

        nums.clear()
        for value in new_nums:
            nums.append(value)