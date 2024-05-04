class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        counter_boats = 0
        total_limit = 0
        people = sorted(people)
        next_number = 0

        i = 0
        j = len(people)-1
        counter_boats = 0

        while(i<=j):
            if people[j]+people[i] <= limit:
                i+=1
            j-=1
            counter_boats+=1
                
        return counter_boats