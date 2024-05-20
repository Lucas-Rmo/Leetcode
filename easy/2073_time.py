class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        counter = 0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[i] !=0:
                    tickets[i] -=1
                    counter +=1
                if tickets[k] == 0:
                    break
        
        return counter
