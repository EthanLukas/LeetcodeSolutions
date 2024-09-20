class Solution:
    
    def romanToInt(self, s: str) -> int:

        vals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        total = 0

        ind = 0

        while ind < len(s):
        
            currVal = s[ind]

            if ind < len(s)-1 and currVal in ["I","X","C"]:

                    nextVal = s[ind+1]
                    
                    # Subtraction case
                    if vals[currVal] < vals[nextVal]:
                        total += (vals[nextVal] - vals[currVal])
                        ind += 1

                    else:
                        total += vals[currVal]
            
            else:
                total += vals[currVal]

            ind += 1

        return total
                            
                        

                