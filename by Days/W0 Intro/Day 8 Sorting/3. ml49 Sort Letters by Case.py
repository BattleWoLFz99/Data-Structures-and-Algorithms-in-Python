from typing import (
    List,
)

class Solution:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars: List[str]):
        if not chars:
            return 
        self.quick_sort(chars, 0, len(chars) - 1)

    def quick_sort(self, chars, start, end):
        if start >= end:
            return

        pivot = self.convert(chars[(start + end) // 2])
        left, right = start, end
        while left <= right:
            while left <= right and self.convert(chars[left]) < pivot:
                left += 1
            while left <= right and self.convert(chars[right]) > pivot:
                right -= 1
            if left <= right:
                chars[left], chars[right] = \
                chars[right], chars[left]
                left += 1
                right -= 1

        self.quick_sort(chars, start, right)
        self.quick_sort(chars, left, end)

    def convert(self, char):
        if char.islower():
            return ord(char) - 97
        return ord(char)