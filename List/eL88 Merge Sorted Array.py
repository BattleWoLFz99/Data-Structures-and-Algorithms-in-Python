# Modified Version, if return a list

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        lst = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums[j]:
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            lst.append(nums1[i])
            i += 1
            
        while j < len(nums1):
            lst.append(nums1[j])
            j += 1     

        return lst  