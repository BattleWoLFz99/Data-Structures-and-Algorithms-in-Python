# Retard if you wanted to convert to string/list

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        return number % 10 * 100 + number // 10 % 10 * 10 + number // 100