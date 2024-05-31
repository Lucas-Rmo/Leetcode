class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums2 = []
        for number in nums:
            if nums.count(number) == 1 :
                nums2.append(number)
    
        return nums2
