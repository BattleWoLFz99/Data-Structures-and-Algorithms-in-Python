# Recursion

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b

        # not needed, delete not recommended
        if n == 1:
            return a % b

        power = self.fastPower(a, b, n // 2)
        power = (power * power) % b

        if n % 2 == 1:
            power = (power * a) % b

        return power


# non-Resursion
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
            
        return ans % b