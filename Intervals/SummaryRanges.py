class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        result = []

        if len(nums) == 0:
            return result

        start = nums[0]
        curr = nums[0]

        ind = 0

        while ind < len(nums):

            if (ind+1 >= len(nums)) or (nums[ind+1] != curr + 1):
                
                if start == curr:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{curr}")
                
                if ind+1 < len(nums):
                    start = nums[ind+1]
                    curr = nums[ind+1]
                else:
                    return result
                

            elif nums[ind+1] == curr + 1:
                curr = nums[ind+1]

            ind+=1
            

        return result