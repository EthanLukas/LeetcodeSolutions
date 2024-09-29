class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        ctr = 0

        # i = 0
        # j = 1
        # k = 2

        hashMap = dict()

        for num in nums:
            hashMap[num] = num - diff

        # while i != j and j != k:

        #     firstDiff = nums[j] - nums[i]
        #     secondDiff = nums[k] - nums[j]

        #     if i < j and j < k  and firstDiff == diff and secondDiff == diff: 
        #         ctr += 1

        print(hashMap)

        for i in range(2, len(nums)):
            
            try:
                firstInd = nums[:i].index(hashMap[nums[i]])
                if firstInd > 0:
                    secondInd = nums[:firstInd].index(hashMap[nums[firstInd]])
                    ctr+=1

            except:
                pass

        return ctr

            
            