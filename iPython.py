# 0. Always start with asking questions:
    # Edge cases
    # Maybe some comments
    # Code Quality
    # Bug Free
    # Logicality
    # perhaps ask: “Would you like me to add comments to this?

    # iBinarySearch.py line 15 is elif, then else

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

# 4. Always use 
    result = max(result, i)

# 5. string is None does not work
    if string == "":
        return 0

# 6. enumerate()


# Python program to illustrate
# enumerate function in loops
l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
print
# changing index and printing separately
for count,ele in enumerate(l1,100):
    print (count,ele)

Output: 
(0, 'eat')
(1, 'sleep')
(2, 'repeat')

100 eat
101 sleep
102 repeat