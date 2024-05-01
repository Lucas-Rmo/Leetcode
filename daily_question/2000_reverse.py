class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse = []
        reversed = []
        reversed_word = ""
        letter_index = 0
        index_counter = 0
        for i in range(len(word)):
            if word[i] == ch:
                letter_index = i
                break

        index_counter = letter_index

        for letter in word:
            reverse.append(letter)
            reversed.append(letter)
        if letter_index == 0:
            return word

        for i in range(letter_index + 1):
            reversed[i] = reverse[index_counter]
            index_counter -=1
        
        for letter in reversed:
            reversed_word +=letter
        return reversed_word
