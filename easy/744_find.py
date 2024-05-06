class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters_list = []
        letters_list.append(target)

        for letter in letters:
            if letter not in letters_list:
                letters_list.append(letter)

        letters_list = sorted(letters_list)

        try:
            for i in range(len(letters_list)):
                if letters_list[i] == target:
                    return letters_list[i+1]
        except:
            return letters_list[0]
