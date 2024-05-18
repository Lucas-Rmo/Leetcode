class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        counter = 1
        
        for i in range(n):
            if i!=0 and i%7 == 0:
                counter = 0
                counter = int(i/7 + 1)
            
            total += counter
            counter += 1

        return total
