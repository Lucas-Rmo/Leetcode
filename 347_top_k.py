class Solution(object):
    def topKFrequent(self, nums, k):
           
        nums2 = []
        returned_list = []
        frequent = {}

        for number in nums:
            if number not in nums2:
                nums2.append(number)
        for number in nums2:
            frequent[number] = nums.count(number)

        sorted_frequency = sorted(frequent.items(),key=lambda item: item[1],reverse = True)

        for i in range(k):
            value = str(sorted_frequency[i])
            value1,value2 = value.split(",")
            value1 = value1.replace("(","")
            returned_list.append(int(value1))
        return returned_list
            
solution = Solution()
print(solution.topKFrequent([1,1,2,2,2,2,3,3,3,3,3,3],2))