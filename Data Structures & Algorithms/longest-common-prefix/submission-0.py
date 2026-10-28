class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
            long_pre = strs[0]
            for j in range(1, len(strs)):
                new_pre = ""
                for l in range(len(long_pre)):
                    if l>=len(strs[j]) or long_pre[l] != strs[j][l]:
                        break
                    new_pre += long_pre[l]
                long_pre = new_pre
            return long_pre
