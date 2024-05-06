class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for number in bin(n):
            if number == "1":
                counter +=1
        
        return counter
