class Solution:
        
    def integerReplacement(self, n: int) -> int:
        
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2

        # Even
        if n % 2 == 0:
            # if (n//2) in memo:
            #     return 1 + memo(n//1)
            # else:
                # memo[n//2] = self.integerReplacement(n//2)
                return 1 + self.integerReplacement(n//2)

        # Odd
        else:
            # if (n+1) in memo:
            #     val1 = memo(n//1)
            #     val2 = memo(n//1)
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))


        