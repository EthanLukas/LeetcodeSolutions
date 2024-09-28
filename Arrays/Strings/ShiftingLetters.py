class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        def shift(self, letter: str) -> str:
            if letter == 'z':
                return 'a'
            else:
                return chr(ord(letter) + 1)

        retString = ""

        total = sum(shifts)

        ind = 0

        while ind < len(s):

            originalLetter = s[ind]

            print(originalLetter)

            tempNum = total%26

            for i in range(tempNum):
                originalLetter = shift(self, originalLetter)

            retString += originalLetter

            total -= shifts[ind]
            ind += 1 

        return retString




            
