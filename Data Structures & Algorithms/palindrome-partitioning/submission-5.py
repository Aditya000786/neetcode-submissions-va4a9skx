class Solution:
    def partition(self, s: str) -> List[List[str]]:
        print("s", s)
        ans = []
        curr = []
        def is_pali(start, end):
            while start<=end and s[start] == s[end]:
                start += 1
                end -= 1
            return True if start>=end else False

        def find_pali(ind):
            if ind>=len(s):
                ans.append(curr.copy())

            for i in range(ind, len(s)):
                if is_pali(ind, i):
                    curr.append(s[ind:i+1])
                    find_pali(i+1)
                    curr.pop()
        find_pali(0)
        return ans