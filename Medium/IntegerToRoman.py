class Solution:
    def intToRoman(self, num: int) -> str:

        returnStr = ""

        if int(str(num)[0]) not in [4,9]:
            if num >= 1000:
                return returnStr + "M" +  self.intToRoman(num-1000)
            elif num >= 500:
                return returnStr + "D" +  self.intToRoman(num-500)
            elif num >= 100:
                return returnStr + "C" +  self.intToRoman(num-100)
            elif num >= 50:
                return returnStr + "L" +  self.intToRoman(num-50)
            elif num >= 10:
                return returnStr + "X" +  self.intToRoman(num-10)
            elif num >= 5:
                return returnStr + "V" +  self.intToRoman(num-5)
            elif num >=1:
                return returnStr + "I" +  self.intToRoman(num-1)
        
        # Starts with 4 or 9
        else:
            if num >= 900:
                return returnStr + "CM" +  self.intToRoman(num-900)
            elif num >= 400:
                return returnStr + "CD" +  self.intToRoman(num-400)
            elif num >= 90:
                return returnStr + "XC" +  self.intToRoman(num-90)
            elif num >= 40:
                return returnStr + "XL" +  self.intToRoman(num-40)
            elif num >= 9:
                return returnStr + "IX" +  self.intToRoman(num-9)
            elif num >= 4:
                return returnStr + "IV" +  self.intToRoman(num-4)

        return returnStr
        





