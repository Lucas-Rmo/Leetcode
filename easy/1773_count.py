class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        index = 0
        counter = 0
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
        
        for i in range(len(items)):
            if items[i][index] == ruleValue:
                counter +=1

        return counter
