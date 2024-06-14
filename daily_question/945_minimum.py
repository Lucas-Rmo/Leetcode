""" Deu quase certo,porém dá time limit nos últimos problemas
class Solution(object):
    def minIncrementForUnique(self, nums):
        counter = 0
        new_list = []

        for i in range(len(nums)):
            if nums[i] not in new_list:
                new_list.append(nums[i])
            elif nums[i] in new_list:
                while nums[i] in new_list:
                    nums[i] +=1
                    counter +=1
                    if nums[i] not in new_list:
                        new_list.append(nums[i])
                        break
        return counter

        """

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # nums = [3,2,1,2,1,7]
        #        [1,1,2,2,3,7]

        # mySet = set({ num for num in nums }), 2+4
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament
