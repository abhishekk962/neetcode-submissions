class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and s == t:
            return True
        if len(s) != len(t):
            return False
        if len(s) == len(t):
            ds = dict()
            for cs in s:
                if cs not in ds:
                    ds[cs] = 0
                else:
                    ds[cs] += 1
            dt = dict()
            for ct in t:
                if ct not in dt:
                    dt[ct] = 0
                else:
                    dt[ct] += 1     
            if ds == dt:
                return True
            else:
                return False
        return False