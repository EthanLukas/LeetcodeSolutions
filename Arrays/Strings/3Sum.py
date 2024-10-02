class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        retSet = set()

        sortedNums = sorted(nums)

        # print(sortedNums)

        # [-2, 0, 1, 1, 2]

        for i in range(0, n-2):
            l = i+1
            r = n-1

            while l < r:
                # print(l, r)

                twoSum = sortedNums[l] + sortedNums[r]

                total = twoSum + sortedNums[i]

                # Triplet
                if total == 0:
                    addList = [sortedNums[i], sortedNums[l], sortedNums[r]]
                    addListS = tuple(sorted(addList))
                    retSet.add(addListS)
                    
                    l+=1
                    r-=1

                elif total > 0:
                    r -= 1

                elif total < 0:
                    l += 1



        # l = 0
        # r = n-1

        # while l < r:

        #     twoSum = sortedNums[l] + sortedNums[r]

        #     find = 0 - twoSum

        #     # Triplet found
        #     if find in sortedNums[l+1:r]:
        #         print(twoSum, find)
        #         addList = [find, sortedNums[l], sortedNums[r]]
        #         addListS = tuple(sorted(addList))
        #         retSet.add(addListS)

        #     if twoSum < 0:
        #         l += 1

        #     elif twoSum > 0:
        #         r -= 1



        return list(retSet)


