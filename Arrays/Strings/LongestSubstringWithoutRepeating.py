class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n==0:
            return 0
        elif n==1:
            return 1

        # Sliding window

        l = 0
        r = 2

        maxUnique = 0

        while (r <= n) and (l != r):
            sub = s[l:r]

            lenSub = len(sub)

            if len(set(sub)) == lenSub:

                if lenSub > maxUnique:
                    maxUnique = lenSub

                r += 1
            
            else:

                l+=1
        
        return maxUnique
