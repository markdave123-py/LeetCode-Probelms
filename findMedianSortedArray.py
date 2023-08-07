class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findi(a:List[int], b:List[int], i:int)->int:
            m,n = len(a), len(b)
			
            if m==0: return b[i]
            if n==0: return a[i]
			
            p=m//2+1
            q=n//2+1

            if a[p-1]>=b[q-1]:
                if i<=p+q-2: return findi(a[:p-1], b, i)
                else: return findi(a, b[q:], i-q)
				
            else:
                if i<=p+q-2: return findi(a, b[:q-1], i)
                else: return findi(a[p:], b, i-p)
            
        l1=len(nums1)
        l2=len(nums2)
        if (l1+l2)%2==1: return findi(nums1, nums2, (l1+l2)//2)
        else: 
            return (findi(nums1, nums2, (l1+l2)//2-1)+findi(nums1, nums2, (l1+l2)//2))/2