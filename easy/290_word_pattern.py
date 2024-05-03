class Solution(object):
    def wordPattern(self, pattern, s):
        list_s = s.split()
        pattern_list = []
        list_s_no_dup = []
        check_pattern = ""
        for letter in pattern:
            if letter not in pattern_list:
                pattern_list.append(letter)
        
        for word in list_s:
            if word not in list_s_no_dup:
                list_s_no_dup.append(word)
        try:
            for word in list_s:
                if word in list_s_no_dup:
                    for i in range(len(list_s_no_dup)):
                        if word == list_s_no_dup[i]:
                            check_pattern += (pattern_list[i])
        except:
            pass
            
        return check_pattern == pattern
solution = Solution()
print(solution.wordPattern( "aaaa","dog dog dog dog"))