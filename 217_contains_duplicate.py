#funciona,mas dá limit time exceeded,pois usa brute force
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums2 = []
        for number in nums:
            if number not in nums2:
                nums2.append(number)
            else:
                return True
        return False
    
#funciona e não dá limit time exceeded
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums2 = set()
        for i in range(len(nums)):
            if nums[i] in nums2:
                return True
            nums2.add(nums[i])
        return False