class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        n = len(s)

        d = dict()
        dt = dict()

        for i in range(n):
            
            sLetter = s[i]
            tLetter = t[i]

            # if sLetter != tLetter:

            if sLetter not in d and tLetter not in dt:
                d[sLetter] = tLetter
                dt[tLetter] = sLetter

            elif sLetter in d and tLetter in dt:
                if d[sLetter] != tLetter or dt[tLetter] != sLetter:
                    return False

            elif tLetter not in dt:
                if d[sLetter] != tLetter:
                    return False
                dt[tLetter] = sLetter

            else:
                if dt[tLetter] != sLetter:
                    return False

                d[sLetter] = tLetter

        # else:
        #     d[sLetter] = tLetter
        #     dt[tLetter] = sLetter

        return True



