class Solution:

    def __init__(self):
        self.memo = dict()
        
    def integerReplacement(self, n: int) -> int:

        if n in self.memo:
            return self.memo[n]
        
        if n == 1:
            self.memo[1] = 0
            return 0
        elif n == 2:
            self.memo[2] = 1
            return 1
        elif n == 3:
            self.memo[3] = 2
            return 2

        # Even
        if n % 2 == 0:
            valRet = 1 + self.integerReplacement(n//2)
            self.memo[n] = valRet
            return valRet

        # Odd
        else:
            valRet = 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
            self.memo[n] = valRet
            return valRet


        