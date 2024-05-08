class Solution(object):
    def sortColors(self, nums):
        #order = red,white and blue ( 0,1,2)
        counter0 = 0 #red
        counter1 = 0 #white
        counter2 = 0 # blue

        for value in nums:
            if value == 0:
                counter0 +=1
            elif value ==1:
                counter1 +=1
            elif value ==2:
                counter2 +=1

        nums.clear()
        while counter0 + counter1 + counter2 > 0:
            if counter0 > 0:
                counter0 -=1
                nums.append(0)
            if counter0 == 0 and counter1 > 0:
                counter1 -=1
                nums.append(1)
            if counter1 == 0 and counter2 > 0:
                counter2 -=1
                nums.append(2)
            
        nums = nums.sort()
