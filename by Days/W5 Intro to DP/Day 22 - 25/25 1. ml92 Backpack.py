# Not final, only for easy undetstanding

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not A:
            return 0

        # states
        n = len(A)

        # initialize:
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # function
        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # answer
        for i in range(m, -1, -1):
            if dp[n][i]:
                return i

        return -1


# or less code...(Same Logic extended to 0)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not A:
            return 0
        # states
        n = len(A)

        # initialize:
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # function
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # answer
        for i in range(m, -1, -1):
            if dp[n][i]:
                return i

        return -1

# 明面上的变形也很多，例如有100元想用得差不多

