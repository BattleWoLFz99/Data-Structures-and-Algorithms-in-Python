# 普通递归
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverseBits(self, n, pos=32):
        if pos == 1:
            return n

        last = n & 1
        ret = self.reverseBits(n >> 1, pos - 1)
        result = (last << (pos - 1)) + ret
        return result


# 尾递归版本
    def reverseBits(self, n, pos=32, result=0):
        if pos == 1:
            return n + result

        last = n & 1
        result += last << (pos - 1)
        return self.reverseBits(n >> 1, pos - 1, result)


# 尾递归迭代
    def reverseBits(self, n, pos=32, result=0):
        while True:
            if pos == 1:
                return n + result

            last = n & 1

            new_n, new_pos = n >> 1, pos - 1
            new_result = result + (last << (pos - 1))
            
            n, pos = new_n, new_pos
            result = new_result