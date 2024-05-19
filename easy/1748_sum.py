class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_nums = []
        nums_sum = 0
        for number in nums:
            if nums.count(number) == 1:
                unique_nums.append(number)

        for number in unique_nums:
            nums_sum += number
        
        
        return nums_sum

        
