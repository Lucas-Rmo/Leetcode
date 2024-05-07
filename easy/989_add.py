class Solution(object):
    def addToArrayForm(self, num, k):
        sys.set_int_max_str_digits(12000)
        number = ""
        total = 0
        number_list = []
        for value in num:
            number += str(value)
        
        number = int(number)
        total = number + k

        for value in str(total):
            number_list.append(int(value))

        return number_list
