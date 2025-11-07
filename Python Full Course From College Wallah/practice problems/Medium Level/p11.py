class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort()  

        first_str = strs[0]
        last_str = strs[-1]
        common_prefix = ""

        for i in range(min(len(first_str), len(last_str))):  
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break

        return common_prefix   
