class Solution(object):
    def plusOne(self, digits):
       total_value = ""
       values = []
       for number in digits:
           total_value +=str(number)
       total_value = int(total_value)+1 
       total_value = str(total_value)
       for i in range(len(total_value)):
           values.append(total_value[i])

       return values
           
solution = Solution()
print(solution.plusOne([9]))