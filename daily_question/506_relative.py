class Solution(object):
    def findRelativeRanks(self, score):
        list_scores = []
        for value in score:
            list_scores.append(value)
        list_scores.sort(reverse=True)
        list_positions = []
        dict_scores = {}
        
        for i in range(len(list_scores)):
            if i ==0:
                dict_scores[list_scores[i]] = "Gold Medal"
            elif i==1:
                dict_scores[list_scores[i]] = "Silver Medal"
            elif i==2:
                dict_scores[list_scores[i]] = "Bronze Medal"
            else:
                dict_scores[list_scores[i]] = str(i +1)
        
        for number in score:
            list_positions.append(dict_scores[number])

        return list_positions
