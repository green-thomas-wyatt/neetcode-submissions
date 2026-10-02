class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We need to find median of list 1
        # then see where it fits in list 2?
        # Then get that median?


        # we could find median of smaller one
        # then see where it fits in bigger one?
        # We can see if list is even or odd also
        # that may influece things

        # lets do 2 pointer approach

        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1):
                median2 = median1
                if i < len1 and j < len2:
                    if nums1[i] > nums2[j]:
                        median1 = nums2[j]
                        j+=1
                    else:
                        median1 = nums1[i]
                        i+= 1
                elif i < len1:
                    median1 = nums1[i]
                    i+= 1     
                else:
                    median1 = nums2[j]
                    j+= 1           
        # Even or Odd?
        if(len1+len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0

        

