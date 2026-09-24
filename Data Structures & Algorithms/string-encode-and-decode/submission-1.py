class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ["---"] * 100
        for i in range(len(strs)):
            lengths[i] = ("000"+str(len(strs[i])))[-3:]

        return "".join(lengths) + "".join(strs)


    def decode(self, s: str) -> List[str]:
        prefix = []
        for i in range(100):
            if s[3*i:3*i+3] != "---":
                prefix.append(int(s[3*i:3*i+3]))
            else:
                break

        index = 300

        res = []

        for p in prefix:
            res.append(s[index:index+p])
            index += p

        return res