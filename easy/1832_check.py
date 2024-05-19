class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = 0
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        unique_alphabet = []

        for letter in sentence:
            if letter in alphabet and letter not in unique_alphabet:
                unique_alphabet.append(letter)

        if len(unique_alphabet) == 26:
            return True
        else:
            return False
