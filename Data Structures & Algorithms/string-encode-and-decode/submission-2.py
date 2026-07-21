class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        
        for s in strs:
            if len(s) >= 100:
                res += str(len(s))+'#'+s
            elif len(s) >= 10:
                res += str(len(s))+'*'+s
            else:
                res += str(len(s))+'-'+s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            if s[i] == '-': # 0-9
                strlen = int(s[i-1])
            elif s[i] == '*': # 10-99
                strlen = int(s[i-2]+s[i-1])
            elif s[i] == '#': # 100-200
                strlen = int(s[i-3] + s[i-2] + s[i-1])

            if s[i] == '-' or s[i] == '*' or s[i] == '#':
                word = ''
                for j in range(strlen):
                    word += s[i+j+1]
                res.append(word)
                i += strlen
                print(f"strlen:{strlen}")
            print(f"i:{i}")
            
            i+=1
        return res
