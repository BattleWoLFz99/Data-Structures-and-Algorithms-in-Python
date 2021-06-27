class Solution:
    # @param {string} str a string
    # @return {string} a compressed string
    def compress(self, str):
        # Write your code here
        if len(str) == 0:
            return str 
        ans = []
        count = 1
        last = str[0]
        for c in str[1:]:
            if c == last:
                count += 1
            else:
                ans.append(last)
                ans.append("%s" % count)
                last = c
                count = 1

        ans.append(last)
        ans.append("%s" % count)

        if len(ans) < len(str):
            return ''.join(ans)
        else:
            return str