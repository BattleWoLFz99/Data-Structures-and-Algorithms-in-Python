class Solution:
    """
    @param secret: An string
    @param guess: An string
    @return: An string
    """
    def getHint(self, secret, guess):
        a, b = 0, 0
        secret_count = dict()
        guess_count = dict()

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

        for i in range(10):
            secret_count.setdefault(str(i), 0)
            guess_count.setdefault(str(i), 0)
            b += min(secret_count[str(i)], guess_count[str(i)])

        return str(a) + 'A' + str(b - a) + 'B'


# 另一种计数方法，与 字母用长度为26的list一样：
    def getHint(self, secret, guess):
        a, b = 0, 0
        ds = [0 for _ in range(10)]
        dg = [0 for _ in range(10)]
        for i in range(len(secret)):
            x = ord(secret[i]) - ord('0')
            y = ord(guess[i]) - ord('0')
            if x == y:
                a += 1
            ds[x] += 1
            dg[y] += 1
        for i in range (10) :
            b += min(ds[i], dg[i])
        return str(a) + 'A' + str(b - a) + 'B'
