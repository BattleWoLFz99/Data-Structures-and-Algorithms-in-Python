class Solution:
    """
    @param string: A string
    @return: whether the string is a valid parentheses
    """
    def matchParentheses(self, string):
        matched = 0
        for parenthese in string:
            if parenthese == '(':
                matched += 1
            else:
                matched -= 1
            if matched < 0:
                return False
        return matched == 0