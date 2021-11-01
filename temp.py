class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        if n <= 0:
            return []

        output = []
        
        for i in range(1, n + 1):
            output.append(str(i))

        for i in range(2, 3):
            print(i)
            output[i] = "fizz"

        for i in range(4, n + 1, 5):
            print(i)
            if output[i] == "fizz":
                output[i] = "fizz buzz"
                continue
            output[i] = "buzz"

        return output

s = Solution()
print(s.fizzBuzz(9))

