class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        i = 0
        while True:
            i +=1 
            if i not in arr:
                counter +=1
            if counter == k:
                return i
