class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr3 = []
        arr4 = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr3.append(arr2[i])

        for i in range(len(arr1)):
            if arr1[i] not in arr3:
                arr4.append(arr1[i])
                
        arr4=sorted(arr4)

        for number in arr4:
            arr3.append(number)
        return arr3
    
solution = Solution()
print(solution.relativeSortArray([28,6,22,8,44,17], arr2 = [22,28,8,6]))