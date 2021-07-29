class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..':
                if len(stack):
                    stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
        return '/' + '/'.join(stack)