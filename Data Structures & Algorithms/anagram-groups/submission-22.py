class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #map string counts to list of strings with that count
        mapping = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            mapping[tuple(count)].append(s)
        return list(mapping.values())