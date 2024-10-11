class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        sCtr = 0
        # tCtr = 0

        for i in range(len(t)):
            if sCtr == len(s):
                return True

            if t[i] == s[sCtr]:
                sCtr+=1

        if sCtr == len(s):
            return True
        return False