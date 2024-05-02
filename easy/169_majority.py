class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = 0
        majority = 0
        no_repeat = []
        for number in nums:
            if number not in no_repeat:
                no_repeat.append(number)
        for number in no_repeat:
            if nums.count(number) > counter:
                counter = nums.count(number)
                majority = number
        return majority
