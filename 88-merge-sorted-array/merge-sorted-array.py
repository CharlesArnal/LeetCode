class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        i2 = n-1
        ic = n+m-1
        while i1>-1 or i2>-1:
            # print(f"{i1} {i2} {ic}")
            a = nums1[i1] if i1 >-1 else -float('inf')
            b = nums2[i2] if i2 >-1 else -float('inf')
            # print(f"{a} {b}")
            if a<=b:
                i2 -= 1
                nums1[ic]=b
            else:
                i1 -= 1
                nums1[ic]=a
            ic -= 1

        