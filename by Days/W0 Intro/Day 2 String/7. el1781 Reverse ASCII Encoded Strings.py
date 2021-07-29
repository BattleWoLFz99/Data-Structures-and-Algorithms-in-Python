class Solution:
    """
    @param encodeString: an encode string
    @return: a reversed decoded string
    """
    def reverseAsciiEncodedString(self, encodeString):
        results = []
        for i in range(0, len(encodeString), 2):
            results.append(chr(int(encodeString[i:i + 2])))
        return "".join(reversed(results))