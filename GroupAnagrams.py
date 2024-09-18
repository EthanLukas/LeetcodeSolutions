class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # groupAnagrams = []

        # # Each iteration collects one group of anagrams
        # while len(strs) > 0:
            
        #     currGroup = [strs[0]]

        #     if len(strs) == 1:
        #         groupAnagrams.append(currGroup)
        #         break
            
        #     currAnagram = ''.join(sorted(strs[0]))

        #     strs.pop(0)

        #     i = 0
        #     while i<len(strs):
        #         val = strs[i]
        #         if ''.join(sorted(val)) == currAnagram:
        #             currGroup.append(strs[i])
        #             strs.pop(i)
        #         else:
        #             i+=1

        #     groupAnagrams.append(currGroup)
            
        # return groupAnagrams



        alteredStrs = []
        groupAnagrams = []

        for ind, st in enumerate(strs):
            st = ''.join(sorted(st))
            alteredStrs.append((ind, st))

        alteredStrs = sorted(alteredStrs, key = lambda x: x[1])

        # print(alteredStrs)

        currGroup = []
        currVal = alteredStrs[0][1]

        for i in alteredStrs:
            tupInd = i[0]
            tupStr = i[1]

            if tupStr == currVal:
                currGroup.append(strs[tupInd])

            else:
                groupAnagrams.append(currGroup)

                currGroup = [strs[tupInd]]
                currVal = tupStr
                # print(currVal)

        groupAnagrams.append(currGroup)
        
        return groupAnagrams

