class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(chr(len(s))) #encode length
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            strlen = ord(s[i]) #decode length
            res.append(s[i+1 : i+1 + strlen])
            i += 1+strlen
        return res