class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for st in strs:
            l = len(st)
            ans += str(l) + "|" + st
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        curr_ind = 0
        while curr_ind<len(s):
            start_word_ind = curr_ind+1
            while s[start_word_ind]!='|':
                start_word_ind+=1
            num_of_chars = int(s[curr_ind: start_word_ind])
            start_word_ind+=1
            curr_word = s[start_word_ind: start_word_ind+num_of_chars]
            ans.append(curr_word)
            curr_ind = start_word_ind+num_of_chars
        return ans


# Solution1:
# Count the chars in each word
# Append the count and then a delimiter and then the word
# So ["neet","code","love","you"] would become:
# 4|neet4|code4|love3|you
# Parse the above string as:
# Parse the num untill u found the delimiter, convert it to int and then parse that many chars
