class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1


        # Length is greater than 2

        result = 0

        l = 0

        r = 2

        # Condition : if k in counts of characters
        # Or comparing pointer locations
        # Maximum character, window length - forgiveness

        d = dict()

        currStr = s[l:r]

        for letter in currStr:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        # Dictionary with current string

        while (r <= len(s)) or (l == r):

            # print("L: ", l, " R: ", r)

            totalLetters = sum(d.values())
            maxNum = max(d.values())

            changeNum = totalLetters - maxNum

            # Enough to change - valid
            if changeNum <= k:
                if len(currStr) > result:
                    # print(currStr)
                    result = len(currStr)
                # Move right pointer one to the right -  edit dictionary
                if r < len(s):
                    if s[r] in d:
                        d[s[r]] += 1
                    else:
                        d[s[r]] = 1
                r+=1

            # Invalid - move left pointer one - edit dictionary
            else:
                if l < len(s):
                    d[s[l]] -= 1
                l+=1

            currStr = s[l:r]


            # Slide left when - not valid, keep moving until everything inside window is valid
            # Compare to current highest result
            # Use dictionary to find max and remove the max from total number of letters
            # Slide right when works - valid

        # print("Final: ", currStr)
        return result