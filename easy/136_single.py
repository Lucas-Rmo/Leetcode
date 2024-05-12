class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for number in nums:
            if nums.count(number) > 1:
                continue
            else:
                return number
