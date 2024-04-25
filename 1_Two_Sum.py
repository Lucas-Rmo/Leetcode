class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        self.nums = nums
        self.target = target
        actual_number = 0
        next_number = 0

        #pega o número atual
        for i in range(len(nums)):
            actual_number = nums[i]
            try:
                #pega o próximo número,ou seja,a posição i + 1 + j(posição no novo for)
                for j in range(len(nums)):
                    next_number = nums[j+1+i]
                    if actual_number + next_number == target:
                        return i,j+1+i
            except:
                pass
def main():
    solution = Solution()
    print(solution.twoSum([3,2,4],6))

if __name__ == "__main__":
    main()