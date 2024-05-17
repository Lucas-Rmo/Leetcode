class Solution(object):
    def restoreString(self, s, indices):
        shuffled_s = ""
        dict_s = {}

        for i in range(len(indices)):
            dict_s[indices[i]] = s[i]

        for i in range(len(dict_s)):
            for key in dict_s:
                if key == i:
                    shuffled_s += dict_s[i]

        return shuffled_s
