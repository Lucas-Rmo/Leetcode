class Solution(object):
    def heightChecker(self, heights):
        sorted_height = sorted(heights)
        counter = 0
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                counter +=1
        return counter
