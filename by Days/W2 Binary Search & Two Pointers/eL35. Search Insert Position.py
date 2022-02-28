# 对二分法第三重境界的思考：验证一切皆可 OOXX Find First & First Last 然后模板想左右条件
# mid + 1 / mid - 1? 笑死，我连 start = mid 还是 end = mid 都不需要考虑了
# Find First, 直接秒杀
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # find last, right condition:
            # Why 爆炸了？
            # Because 1 3 5 6, 2
            #         O X X X
            # 不满足的时候可以往右一个位置
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if end + 1 < len(nums) and nums[end + 1] <= target:
            return end + 1
        if nums[end] <= target:
            return end
        if start + 1 < len(nums) and nums[start + 1] <= target:
            return start + 1
        if nums[start] <= target:
            return start
        return -1

# Find Last，怎么都爆炸：
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # find last, right condition:
            # Why 爆炸了？
            # Because 1 3 5 6, 2
            #         O X X X
            # 不满足的时候可以往右一个位置
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        # 随你怎么玩，反正一定过不了
        # 你必须复制粘贴 if 里的东西，改都不能改
        if end + 1 < len(nums) and nums[end + 1] <= target:
            return end + 1
        if start + 1 < len(nums) and nums[start + 1] <= target:
            return start + 1
        if nums[end] <= target:
            return end
        if nums[start] <= target:
            return start
        return -1