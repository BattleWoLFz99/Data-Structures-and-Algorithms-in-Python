class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if not S or len(S) < 3:
            return 0

        S.sort()
        ans = 0

        for index in range(2, len(S)):
            ans += self.get_triange_count(S, index)

        return ans

    def get_triange_count(self, S, index):
        cnt = 0
        left, right = 0, index - 1
        target_sum = S[index]

        while left < right:
            if S[left] + S[right] > target_sum:
                cnt += right - left
                right -= 1
            else:
                left += 1

        return cnt