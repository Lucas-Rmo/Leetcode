class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        numbernormal = []
        numberreverse = []
        counter = -1
        for number in str(x):
            numbernormal.append(number)

        for i in range(len(numbernormal)):
            numberreverse.append(numbernormal[counter])
            counter -=1
        if numbernormal == numberreverse:
            return True
        else:
            return False
            
solution = Solution()
print(solution.isPalindrome(121))
        