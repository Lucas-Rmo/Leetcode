class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        numbers = [0,1]
        
        for i in range(1,n+1):
            numbers.append(numbers[i]+numbers[i-1])

        return numbers[i]
            
