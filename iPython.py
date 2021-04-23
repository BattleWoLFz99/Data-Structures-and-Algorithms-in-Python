# 0. Always start with asking questions:
    # Edge cases
    # Maybe some comments
    # Code Quality
    # Bug Free
    # Logicality
    # perhaps ask: “Would you like me to add comments to this?

# 1. Basic Operation:
    >>> 5 / 2
    2.5
    >>> 5//2
    2
    >>> 5 % 2
    1

# 2. You may use higher-order function, or:
    def isPalindrome(self, s, left, right):
        return True

    def validPalindrome(self, s):
        return self.isPalindrome(s, left + 1, right)

# 3. Use of \
    return self.isPalindrome(s, left + 1, right) or\
        self.isPalindrome(s, left, right - 1)
