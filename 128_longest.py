class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(nums)
        counter = 0
        max_counter = 0
        
        for i in range(len(nums)-1):
            
            if nums[i] + 1 == nums[i+1]:
                counter +=1
           
                if counter > max_counter:
                    max_counter = counter
            elif nums[i] == nums[i+1]:
                continue    
            else:        
                counter = 0
                continue
        if len(nums) >= 1:
            max_counter+=1

        return max_counter