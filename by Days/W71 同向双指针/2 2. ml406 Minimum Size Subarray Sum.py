# V1: TLE O(n^2)
# 前缀和求子数组sum: prefix_sum[j + 1] - prefix[i]
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if not nums or sum(nums) < s:
            return -1

        result = float('inf')
        n = len(nums)
        prefix_sum = self.get_prefix_sum(nums)
        for i in range(n):
            for j in range(i, n):
                if prefix_sum[j + 1] - prefix_sum[i] >= s:
                    result = min(result, j + 1 - i)

        if result == float('inf'):
            return -1
        return result

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for i in range(1, len(nums) + 1):
            prefix_sum.append(prefix_sum[i - 1] + nums[i - 1])

        return prefix_sum


# V2: TLE O(n logn)
# 前缀和 + 二分
    def minimumSize(self, nums, s):
        # O(n logn) (not the best)
        if not nums or sum(nums) < s:
            return -1

        result = float('inf')
        n = len(nums)
        prefix_sum = self.get_prefix_sum(nums)
        for i in range(n):
            j = self.get_end(prefix_sum, i, s)
            if prefix_sum[j + 1] - prefix_sum[i] >= s:
                result = min(result, j + 1 - i)

        if result == float('inf'):
            return -1
        return result

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for i in range(1, len(nums) + 1):
            prefix_sum.append(prefix_sum[i - 1] + nums[i - 1])

        return prefix_sum

    def get_end(self, prefix_sum, i, s):
        start, end = i, len(prefix_sum) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if prefix_sum[mid + 1] - prefix_sum[i] >= s:
                end = mid
            else:
                start = mid
        if prefix_sum[start + 1] - prefix_sum[i] >= s:
            return start
        return end


# V3: O(n) 
# 同向双指针(滑动窗口)
    def minimumSize(self, nums, s):
        # O(n logn) (not the best)
        if not nums or sum(nums) < s:
            return -1

        j, ans = 0, float('inf')
        curr_sum = 0
        n = len(nums)
        for i in range(n):
            while j < n and curr_sum < s:
                curr_sum += nums[j]
                j += 1
            if curr_sum >= s:
                ans = min(ans, j - i)
            curr_sum -= nums[i]

        return ans if ans != float('inf') else float('inf')