class Solution:
    def countBits(self, n: int) -> List[int]:
        list_of_1s = []
        
        for i in range(0,n+1):
            counter = 0
            for number in bin(i):
                if number == "1":
                    counter +=1
            list_of_1s.append(counter)
        return list_of_1s
