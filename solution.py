class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=m
        for i in range(0,n):
            nums1[j]=nums2[i]
            k=j
            while(k>0):
                if(nums1[k-1]>nums1[k]):
                    y=nums1[k-1]
                    nums1[k-1]=nums1[k]
                    
                    nums1[k]=y
                    k=k-1
                else:
                    break
                
            j=j+1
