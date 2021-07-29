class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # do not modify original data
        if a > b:
            big, small = a, b
        else:
            big, small = b, a

        while small != 0:
            big, small = small, big % small

        return big


class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        if a > b:
            big, small = a, b
        else:
            big, small = b, a

        if small != 0:
            return self.gcd(small, big % small)
        else:
            return big