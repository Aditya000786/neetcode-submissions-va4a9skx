class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start_end = {}
        Interval = namedtuple('Interval', ['start', 'end'])
        for ind in range(len(s)):
            if s[ind] not in start_end:
                start_end[s[ind]] = Interval(ind, ind)
            else:
                start_end[s[ind]] = Interval(start_end[s[ind]].start, ind)
        res = []
        ind = 0
        while ind < len(s):
            start_ind = ind
            curr_char = s[start_ind]
            end_ind =  start_end[curr_char].end
            chars = set(s[start_ind])
            i = start_ind
            while i < end_ind:
                if s[i] not in chars:
                    end_ind = max(end_ind, start_end[s[i]].end)
                    chars.add(s[i])
                i+=1
            res.append(end_ind - start_ind + 1)
            ind = end_ind+1
        return res



