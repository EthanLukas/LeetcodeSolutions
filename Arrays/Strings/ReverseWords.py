class Solution:
    def reverseWords(self, s: str) -> str:
        
        splitString = (s.strip()).split()

        splitString = splitString[::-1]
        
        return " ".join(splitString)
