class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1 = ""
        s2 = ""
        counter1 = 0
        counter2 = 0

        for i in range(len(s)):
            if i < len(s)/2:
                s1 += s[i]
            else:
                s2 += s[i]

        for letter in s1:
            if letter in vowels:
                counter1 +=1
        
        for letter in s2:
            if letter in vowels:
                counter2 +=1

        return counter1 == counter2

