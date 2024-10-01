class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # Keep the values stored in tuples with distance from the original
        values = []

        for num in arr:
            dist = abs(x-num)

            values.append((num, dist))

        sortedTuples = sorted(values, key=lambda x: (x[1], x[0]))

        # print(sortedTuples)

        result = []

        for i in range(k):
            result.append(sortedTuples[i][0])
        
        return sorted(result)

