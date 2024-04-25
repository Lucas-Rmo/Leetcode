class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        self.strs = strs
        list_prefix = []
        current_prefix = ""
        next_prefix = ""
        one_letter = 0
        if len(strs) == 1:
            return strs[0]
        
        for word in strs:
            if len(word) == 1:
                one_letter = 1
        for word in strs:
            try:
                if one_letter == 0 :
                    prefix = word[0] + word[1]
                    list_prefix.append(prefix)
                elif one_letter ==1 :
                    prefix = word[0]
                    list_prefix.append(prefix)
            except:
                pass

        for i in range(len(list_prefix)):
            current_prefix = list_prefix[i]
            try:
                for j in range(len(list_prefix)-1):
                    next_prefix = list_prefix[j+i+1]
                if current_prefix == next_prefix:
                    return current_prefix
            except:
                pass
        return ""
        
        
        
solution = Solution()
print (solution.longestCommonPrefix(["a"]))