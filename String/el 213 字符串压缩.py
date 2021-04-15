class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        idx1 = 0
        idx2 = 0
        compressedString = ""
        while idx1 < len(originalString) and idx2 < len(originalString):
            # Obivious  and idx2 < len(originalString) is not needed
            count = 0
            while idx2 < len(originalString):
                if originalString[idx1] == originalString[idx2]:
                    idx2 += 1
                    count += 1
                else:
                    break
            compressedString += originalString[idx1]
            compressedString += str(count)
            #idx1 += count
            #idx2 = idx1
            idx1 = idx2
            # Turns out the same, but MUST know why

        # print(originalString)
        # print(compressedString)
        if len(compressedString) < len(originalString):
            return compressedString
        else:
            return originalString

Example 1:
Input: str = "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:
Input: str = "aabbcc"
Output: "aabbcc"