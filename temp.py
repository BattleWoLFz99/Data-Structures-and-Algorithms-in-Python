class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.quickSort(colors, 0, len(colors) - 1)

        return colors

    def quickSort(self, colors, start, end):
        if start == end:
            return
        
        mid = (colors[start] + colors[end]) // 2
        left, right = start, end

        while left <= right:
            while left <= right and colors[left] <= mid:
                left += 1
            while left <= right and colors[right] > mid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
            
        return colors
