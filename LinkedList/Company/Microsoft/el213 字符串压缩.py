class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        idx1, idx2 = 0, 0
        compressedString = ""
        while idx1 < len(originalString) and idx2 < len(originalString):
            # After reading the entire while loop, obviously you don't need to have  and idx2 < len(originalString)
            count = 0
            while idx2 < len(originalString):
                if originalString[idx1] == originalString[idx2]:
                # Obviously you can combine the while loop and if loop
                    idx2 += 1
                    count += 1
                else:
                    break
            compressedString += originalString[idx1]
            compressedString += str(count)
            #idx1 += count
            #idx2 = idx1
            # Same as:
            idx1 = idx2 

        if len(compressedString) < len(originalString):
            return compressedString
        else:
            return originalString