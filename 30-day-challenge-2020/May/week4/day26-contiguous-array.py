# Contiguous Array
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0, 1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0, 1, 0]
# Output: 2
# Explanation: [0, 1](or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50, 000.


##############################################################################################
# Complexity Analysis                                                                        #
# Time Complexity: O(N). The entire array is traversed only once.                            #
# Space Complexity: O(N), Maximum size of the HashMap mapmap will be N,                      #
#                          if all the elements are either 1 or 0                             #
##############################################################################################

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count = 0
        table = {0: -1}
        max_len = 0

        for idx, number in enumerate(nums):
            if number:
                count += 1
            else:
                count -= 1

            if count in table:
                # if there is a subarray with equal number
                # of 0 and 1, than update max length
                max_len = max(max_len, (idx - table[count]))
            else:
                # if not just update the count with indx
                table[count] = idx

        return max_len
