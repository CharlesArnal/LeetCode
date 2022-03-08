from math import ceil 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.auxfun(ceil(float(len(nums1)+len(nums2))/2), (len(nums1)+len(nums2))%2==0, nums1, nums2)
        else:
            return self.auxfun(ceil(float(len(nums1)+len(nums2))/2), (len(nums1)+len(nums2))%2==0, nums2, nums1)
        
    def auxfun(self,n,average,nums1,nums2):
        #print("\n")
        #print(n)
        #print(nums1)
        #print(nums2)
        l1, l2 = len(nums1), len(nums2)
        if l2 == 0 :
            return float(nums1[n-1]+nums1[n])/2 if average else nums1[n-1]
        
        if n==0:
            return min(nums1[0],nums2[0])
        if n==1:
            #print("n==1")
            if nums1[0]>nums2[0]:
                if not average :
                    return nums2[0]
                else:
                    if len(nums2)>=2 and nums2[1]< nums1[0]:
                        return float(nums2[0]+nums2[1])/2
                    else:
                        return float(nums1[0]+nums2[0])/2
            else:
                if not average :
                    return nums1[0]
                else:
                    if len(nums1)>=2 and nums1[1]< nums2[0]:
                        return float(nums1[0]+nums1[1])/2
                    else:
                        return float(nums2[0]+nums1[0])/2

        
        if 2*l2<n :
            if nums2[-1]>nums1[n-l2-1]:
                return self.auxfun(l2,average,nums1[n-l2:],nums2) if l1-n+l2 > l2 else auxfun(l2,average,nums2,nums1[n-l2:])
            else:
                return self.auxfun(n-l2,average,nums1,[])
        else :      
            if nums1[floor(float(n)/2)-1]> nums2[ceil(float(n)/2)-1]:
                if (floor(float(n)/2) if average else floor(float(n)/2)+1) >= l2-ceil(float(n)/2):
                    return self.auxfun(n-ceil(float(n)/2),average,nums1[:(floor(float(n)/2) if not average else floor(float(n)/2)+1)], nums2[ceil(float(n)/2):]) 
                else:
                    return self.auxfun(n-ceil(float(n)/2),average,nums2[ceil(float(n)/2):],nums1[:(floor(float(n)/2) if not average else floor(float(n)/2)+1)]) 
            else:
                #print("this case")
                #print(average)
                if l1-floor(float(n)/2) >=(ceil(float(n)/2) if average else ceil(float(n)/2)+1) :
                    return self.auxfun(n-floor(float(n)/2), average, nums1[floor(float(n)/2):], nums2[:(ceil(float(n)/2) if not average else ceil(float(n)/2)+1)])
                else:
                    return self.auxfun(n-floor(float(n)/2), average, nums2[:(ceil(float(n)/2) if not average else ceil(float(n)/2)+1)], nums1[floor(float(n)/2):])
                
                
#my_sol= Solution()
#my_sol.findMedianSortedArrays([1,2],[1,2,3])