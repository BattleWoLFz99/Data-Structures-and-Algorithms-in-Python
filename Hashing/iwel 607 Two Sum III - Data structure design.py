# You also need to know two pointers solution(TLE, merely for practice)

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.num_to_cnt_map = {}

    def add(self, number):
        # ALWAYS REMEMBER dict.GET(key, defValue)
        self.num_to_cnt_map[number] = self.num_to_cnt_map.get(number, 0) + 1
        

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num1 in self.num_to_cnt_map:
            num2 = value - num1
            num2Cnt = 2 if (num1 == num2) else 1
            if self.num_to_cnt_map.get(num2, 0) >= num2Cnt:
                return True

        return False