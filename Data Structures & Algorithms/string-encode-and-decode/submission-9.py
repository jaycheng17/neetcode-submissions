class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        parts = []
        for word in strs:
            length = len(word)
            parts.append(str(length) + "#")
            parts.append(word)
    
        encoded_string = "".join(parts)

        return encoded_string
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        print (s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            start = j + 1
            length = s[i:j]
            end = start + int(length)

            decoded_strs.append(s[start:end])

            i = end
            

        return decoded_strs
