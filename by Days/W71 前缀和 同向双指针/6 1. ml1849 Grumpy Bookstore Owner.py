class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """
    def maxSatisfied(self, customers, grumpy, X):
        # write your code here
        if not customers or not grumpy:
            return
        
        n = len(customers)
        j, turned_count, max_turned_count = 0, 0, 0
        for i in range(n):
            # i 处理部分：本题 i 不可能跑 j 前面，没有内容;

            while j < n and j - i < X:
                if grumpy[j] == 1:
                    turned_count += customers[j]
                j += 1

            # if 部分：max 不需要担心 j 出去
            # 一般 count 类题目才需要。也不需要优化
            max_turned_count = max(max_turned_count, turned_count)

            # 为下一个 i 做准备。也可以扔 line 16 然后 if i > 0
            if grumpy[i] == 1:
                turned_count -= customers[i]

        original_count = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                original_count += customers[i]

        return original_count + max_turned_count            