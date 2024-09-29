class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = dict()

        # Dict with frequencies
        for word in words:
            if word in d:
                d[word] += 1

            else:
                d[word] = 1

        doubles = []
        
        for key, val in d.items():
            doubles.append((key,val))

        print(doubles)

        sortedDoubles = sorted(doubles, key=lambda x: (-x[1], x[0]))

        print(sortedDoubles)

        limited = sortedDoubles[:k]

        results = [x[0] for x in limited]

        # Lexicographical order
        return results