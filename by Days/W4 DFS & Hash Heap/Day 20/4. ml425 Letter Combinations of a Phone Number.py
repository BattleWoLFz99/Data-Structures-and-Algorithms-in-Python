KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        if not digits:
            return []

        combinations = []
        self.dfs(digits, 0, [], combinations)

        return combinations

    def dfs(self, digits, index, combination, combinations):
        # if index == len(digits)
        if len(combination) == len(digits):
            combinations.append(''.join(combination))
            return

        for letter in KEYBOARD[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()