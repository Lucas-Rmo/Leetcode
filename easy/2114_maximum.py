class Solution(object):
    def mostWordsFound(self, sentences):
        most = 0
        for i in range(len(sentences)):
            words = sentences[i].split()
            if len(words) > most:
                most = len(words)
            words.clear()
        return most
    
