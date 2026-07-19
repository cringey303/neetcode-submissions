class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1 # map chars to 0-26
            
            res[tuple(count)].append(s) # add string to result dict

        return list(res.values())