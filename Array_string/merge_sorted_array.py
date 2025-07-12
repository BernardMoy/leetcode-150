class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # copy_nums1 extract the actual nums1 array
        copy_nums1 = nums1.copy()[: len(nums1) - len(nums2)]

        # Two pointers
        i, j = 0, 0  # i for nums1, j for nums2
        cur = 0  # Pointer for the final result

        while i < len(copy_nums1) and j < len(nums2):
            if nums2[j] <= copy_nums1[i]:
                nums1[cur] = nums2[j]
                j += 1
                cur += 1

            else:
                nums1[cur] = copy_nums1[i]
                i += 1
                cur += 1

        # After the while loop, add remaining elements from the another array
        while i < len(copy_nums1):
            nums1[cur] = copy_nums1[i]
            i += 1
            cur += 1

        while j < len(nums2):
            nums1[cur] = nums2[j]
            j += 1
            cur += 1
