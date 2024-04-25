class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        number = 0
        s_list = []
        current_letter = ""
        next_letter = ""

        for letter in s:
            s_list.append(letter)
        
        for i in range(len(s_list)):
            try:
                current_letter = s_list[i]
                next_letter = s_list[i+1]

                if current_letter == "I" and next_letter == "V":
                    number -=2
                if current_letter == "I" and next_letter == "X":
                    number -=2
                if current_letter == "X" and next_letter == "L":
                    number -=20
                if current_letter == "X" and next_letter == "C":
                    number -=20
                if current_letter == "C" and next_letter == "D":
                    number -=200
                if current_letter == "C" and next_letter == "M":
                    number -=200
            except:
                pass

        for letter in s:
            if letter == "I":
                number +=1
            elif letter == "V":
                number +=5
            elif letter == "X":
                number +=10
            elif letter == "L":
                number +=50
            elif letter == "C":
                number +=100
            elif letter == "D":
                number +=500
            elif letter == "M":
                number +=1000
        
        return number