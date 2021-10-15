class Solution:
    """
    @param answers: some subset of rabbits (possibly all of them) tell 
    @return: the minimum number of rabbits that could be in the forest.
    """
    def numRabbits(self, answers):
        if not answers:
            return 0
        
        total = 0
        d = dict()
        for number in answers:
            d[number] = d.get(number, 0) + 1

        for key, value in d.items():
            num_per_group = key + 1
            reply_count = value
            num_of_group = reply_count // num_per_group
            if reply_count % num_per_group != 0:
                num_of_group += 1
            total += num_of_group * num_per_group

        return total