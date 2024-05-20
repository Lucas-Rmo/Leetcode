class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        list_nums = []
        for number in nums1:
            if number in nums2 and number not in list_nums or number in nums3 and number not in list_nums:
                list_nums.append(number)
        
        for number in nums2:
            if number in nums3 and number not in list_nums:
                list_nums.append(number)

        return list_nums
