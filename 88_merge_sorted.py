class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        new_list = []
        for i in range(m):
            new_list.append(nums1[i])
        for i in range(n):
            new_list.append(nums2[i])
        nums1.clear()
        for value in sorted(new_list):
            nums1.append(value)

 