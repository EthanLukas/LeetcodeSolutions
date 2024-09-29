class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedDict = dict()

        for word in strs:

            sortedWord = str(sorted(word))

            if sortedWord in sortedDict:
                sortedDict[sortedWord].append(word)
            else:
                sortedDict[sortedWord] = [word]

        resultArray = []

        return sortedDict.values()