class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maximum = 0

        n = len(height)

        l = 0
        r = n-1

        while l < r:

            minHeight = min(height[l], height[r])

            currArea = minHeight * (r-l)

            maximum = max(maximum, currArea)

            if height[l] > height[r]:
                r-=1

            else:
                l+=1
        
        return maximum




