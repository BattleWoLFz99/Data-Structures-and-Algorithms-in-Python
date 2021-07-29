# 废话我知道很简单，联系一句话 return，然后不需要 return True if xxx else False 多此一举

class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)