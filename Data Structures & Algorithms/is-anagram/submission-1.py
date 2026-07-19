class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s+t)%2 == 1:
            return False
            
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

        for j in t:
            if j in letters:
                letters[j] -= 1
                if letters[j] < 0:
                    return False
            else:
                return False
        return True