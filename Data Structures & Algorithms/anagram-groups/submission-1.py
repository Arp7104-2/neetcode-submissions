class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countsMap = defaultdict(list)
        for s in strs:
            letterCounts = [0]*26
            for letter in s:
                letterCounts[ord(letter) - 97] += 1
            countsMap[tuple(letterCounts)].append(s)
        return list(countsMap.values())

        