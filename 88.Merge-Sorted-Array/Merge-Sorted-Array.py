class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        padding=len(nums1)-m-n
        mm=len(nums1)-1
        nn=len(nums2)-1
        while mm!=-1:
            if nums1[mm]==0 and len(nums1)>m:
                nums1.pop(mm)
                mm=mm-1
            else:
                break
        while nn!=-1:
            if nums2[nn]==0 and len(nums2)>n:
                nums2.pop(nn)
                nn=nn-1
            else:
                break
        nums1.extend(nums2)
        nums1.sort()
        for i in range(padding):
            nums1.append(0)
    #nums1[m:] = nums2[:n]
    #nums1.sort()             use slice can easliy get the results...