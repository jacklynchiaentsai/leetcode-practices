"""
n = len(strs)
m = len(s)
time:
    encode: O(m) join function
    decode: O(m)
space:
    encode: O(n)
    decode: O(n) we don't consider output as part of space complexity
"""
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for curstr in strs:
            separator = f"{len(curstr)}#"
            res.append(separator)
            res.append(curstr)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        curnum = []
        curIndex = 0
        res = []

        while curIndex < len(s):
            while s[curIndex] != '#':
                curnum.append(s[curIndex])
                curIndex += 1

            charlen = int(''.join(curnum))
            curnum = []
            element = s[curIndex + 1: curIndex + 1 + charlen]
            res.append(element)
            curIndex = curIndex + 1 + charlen
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
"""
["Hello","Wor#ld"]
[5, 6]

5#Hello7#Wor6#ld

encode:
res = []
for each str in strs:
    add len(str) + '#' into res
    add str into res

join res to return encoded string

decode:
curnum = []
curIndex = 0
res = []

while curIndex < len(s):
    while s[curIndex] != '#':
        append curchar into curnum

    convert curnum to integer
    element = s[curIndex + 1: curIndex + 1 + curnum ]
    add element into res
    curnum = []

    curIndex = curIndex + 1 + curnum


"""
