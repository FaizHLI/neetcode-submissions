class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_S = defaultdict(int)
        for c in s:
            count_S[c] +=1
        count_t = defaultdict(int)
        for c in t:
            count_t[c] +=1
        return count_S == count_t