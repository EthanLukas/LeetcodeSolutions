class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        leftPtr = 0
        rightPtr = n-1

        while leftPtr != rightPtr:

            left = numbers[leftPtr]
            right = numbers[rightPtr]

            if left + right == target:
                return [leftPtr+1, rightPtr+1]

            elif left + right > target:
                rightPtr -=1
            
            else:
                leftPtr += 1
        

