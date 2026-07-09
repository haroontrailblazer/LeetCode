"""

4. Median of Two Sorted Arrays
Solved
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
                
            else:
                merged.append(nums2[j])
                j += 1
                
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        n = len(merged)
        
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return float(merged[n // 2-1] + merged[n // 2]) / 2
        
        
""" 
Alternate solution

import numpy as np
merged = sorted(nums1 + nums2)
return np.median(merged)

"""